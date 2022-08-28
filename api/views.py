from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import BlurSerializer


class BlackAndWhite(GenericAPIView):
    def get(self, request, format=None):
        """
        Processing codes goes here!
        """
        return Response({"results": "image converts to B/W!"})


class Blur(GenericAPIView):
    serializer_class = BlurSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        raw_image = serializer.validated_data.get('raw_image')
        rate = serializer.validated_data.get('rate')
        """
        Processing codes goes here!
        """
        return Response({"results": {"image_src": raw_image.name, "rate": "input rate is %d" % rate}})
