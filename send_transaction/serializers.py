from rest_framework import serializers
from .models import Transaction
from web3 import Web3


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    sender = serializers.CharField(max_length=42)
    recipient = serializers.CharField(max_length=42)
    value_sent = serializers.IntegerField()
    private_key = serializers.CharField(max_length=100, write_only=True)

    def create(self, validated_data):
        ganache_url = "http://127.0.0.1:7545"
        web3 = Web3(Web3.HTTPProvider(ganache_url))

        private_key = validated_data["private_key"]
        nonce = web3.eth.getTransactionCount(validated_data["sender"])

        tx = {
            "nonce": nonce,
            "to": validated_data["recipient"],
            "value": web3.toWei(validated_data["value_sent"], "ether"),
            "gas": 2000000,
            "gasPrice": web3.toWei("50", "gwei"),
        }
        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        validated_data.pop("private_key", None)

        return Transaction.objects.create(**validated_data)
