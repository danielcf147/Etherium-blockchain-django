from rest_framework.views import APIView, Response, Request, status
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionView(APIView):
    def get(self, request: Request) -> Response:
        users = Transaction.objects.all()

        serializer = TransactionSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:

        serializer = TransactionSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
