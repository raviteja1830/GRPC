import grpc
#from google.protobuf import empty_pb2
#from django_grpc_framework.services import Service
from blog.models import Post
from blog.serializers import PostProtoSerializer

from django_grpc_framework import mixins
from django_grpc_framework import generics


class PostService(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericService):
    queryset = Post.objects.all()
    serializer_class = PostProtoSerializer

'''class PostService(Service):
    def List(self, request, context):
        posts = Post.objects.all()
        serializer = PostProtoSerializer(posts, many=True)
        for msg in serializer.message:
            yield msg

    def Create(self, request, context):
        serializer = PostProtoSerializer(message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'Post:%s not found!' % pk)

    def Retrieve(self, request, context):
        post = self.get_object(request.id)
        serializer = PostProtoSerializer(post)
        return serializer.message

    def Update(self, request, context):
        post = self.get_object(request.id)
        serializer = PostProtoSerializer(post, message=request)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

    def Destroy(self, request, context):
        post = self.get_object(request.id)
        post.delete()
        return empty_pb2.Empty()'''