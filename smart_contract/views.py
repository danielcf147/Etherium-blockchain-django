from rest_framework.views import APIView, Response, Request, status
from .models import SmartContract
from .serializers import SmartContractSerializer


class SmartContractView(APIView):
    def get(self, request: Request) -> Response:
        users = SmartContract.objects.all()

        serializer = SmartContractSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:

        serializer = SmartContractSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
