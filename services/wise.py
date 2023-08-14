import json
import uuid
from decouple import config
from fastapi import HTTPException
import requests

class WiseService:
    def __init__(self):
        self.main_url="https://api.sandbox.transferwise.tech"
        self.headers={
            "Content-Type":"application/json",
            "Authorization":f"Bearer {config('WISE_TOKEN')}"
        }
        self.profile_id=self.get_profile_id()
    
    def get_profile_id(self):
        url=self.main_url+"/v1/profiles"
        resp=requests.get(url,headers=self.headers)

        if resp.status_code==200:
            resp=resp.json()
            return [el["id"] for el in resp if el["type"]=="personal"][0]
        print(resp)
        raise HTTPException(500,"Payment provider is not available")
    
    def create_quote(self,amount):
        url = self.main_url+"/v2/quotes"
        data = {
            "sourceCurrency":"EUR",
            "targetCurrency":"EUR",
            "sourceAmount":amount,
            "profile":self.profile_id
        }

        resp = requests.post(url, headers=self.headers,data=json.dumps(data))

        if resp.status_code==200:
            resp = resp.json()
            return resp["id"]
        
        print(resp)
        raise HTTPException(500, "Payment provider is not available at the moment!")

    def create_recipient_account(self,full_name,iban):
        url=self.main_url+"/v1/accounts"
        data={
            "currency":"EUR",
            "type":"iban",
            "profile":self.profile_id,
            "accountHolderName":full_name,
            "legalType":"PRIVATE",
            "details":{
                "iban":iban
            }

        }

        resp = requests.post(url, headers=self.headers,data=json.dumps(data))
        if resp.status_code==200:
            resp = resp.json()
            return resp["id"]
        
        print(resp)
        raise HTTPException(500, "Payment provider is not available at the moment!")
    
    def create_transfer(self,target_account_id,quote_id):
        customer_transaction_id=str(uuid.uuid4())
        url = self.main_url+"/v1/transfer"
        data ={
           "targerAccount":target_account_id,
           "quoteUuid" :quote_id,
           "customerTransactionId": customer_transaction_id
        }
        resp = requests.post(url,headers=self.headers,data=json.dumps(data))
        if resp.status_code==200:
            resp = resp.json()
            return resp["id"]
        
        print(resp)
        raise HTTPException(500, "Payment provider is not available at the moment!")
    

    def fund_transfer(self,transfer_id):
        url = self.main_url + f"/v3/profiles/{self.profile_id}/transfers/{transfer_id}/payments"
        data = {
            "type":"BALANCE"
        }

        resp = requests.post(url,headers=self.headers,data=json.dumps(data))
        if resp.status_code==201:
            resp = resp.json()
            return resp["type"]
        
        print(resp)
        raise HTTPException(500, "Payment provider is not available at the moment!")
    
    def cancel_funds(self,transfer_id):
        url=self.main_url+f"/v1/transfers/{transfer_id}/cancel" 
        resp =requests.put(url,headers=self.headers)
        if resp.status_code==200:
            resp = resp.json()
            return resp["id"]
        
        print(resp)
        raise HTTPException(500, "Payment provider is not available at the moment!")

        
if __name__=="__main__":
    wise=WiseService()
    res=wise.create_quote(50)
    a=5



    


