# todo > views.py
from rest_framework import status, viewsets
# 일반적인 CRUD 개발에는 ViewSet을 사용하지만 Todo 완료 및 조회 기능이 있기 때문에 APIView를 사용한다
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSimpleSerializer

# 전체 조회 뷰는 GET방식으로 요청 처리
class TodosAPIView(APIView):
    def get(self, request):
        # get메소드에서 complete=False인 Todo들을 필터링, 시리얼라이저를 통과시켜 보낼 수 있는 형태로 변환
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSimpleSerializer(todos, many=True)
        # 변환한 것을 Response 객체 형태로 전달한다
        return Response(serializer.data, status = status.HTTP_200_OK)