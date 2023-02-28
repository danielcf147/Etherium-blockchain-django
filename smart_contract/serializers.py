from rest_framework import serializers
from .models import SmartContract
from web3 import Web3
import json


class SmartContractSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    sender = serializers.CharField(max_length=42)
    newName = serializers.CharField(max_length=127)
    address = serializers.CharField(max_length=100, write_only=True)

    def create(self, validated_data):
        ganache_url = "http://127.0.0.1:7545"
        web3 = Web3(Web3.HTTPProvider(ganache_url))

        web3.eth.defaultAccount = validated_data["address"]

        abi = json.loads(
            '[{"inputs":[],"name":"nameToRegister","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"newName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"returnNewName","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_newName","type":"string"}],"name":"setNameToRegister","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
        )
        address = web3.toChecksumAddress("0x27DB45c4168Df814D8E0945888137cA6937e338e")

        contract = web3.eth.contract(address=address, abi=abi)

        tx_hash = contract.functions.setNameToRegister(
            validated_data["newName"]
        ).transact()

        web3.eth.waitForTransactionReceipt(tx_hash)

        validated_data.pop("address", None)

        return SmartContract.objects.create(**validated_data)
