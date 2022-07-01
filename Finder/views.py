from django.shortcuts import render
from .serializers import SearchSerializer
from rest_framework.views import APIView 
from .search_music import MusicScraper
from rest_framework import status
from rest_framework.response import Response


Searcher = MusicScraper()


# class SearchDetailLinkAPI(APIView):
#     def get(self, request, slug):
#         results = Searcher.fa_search(slug)
#         serializer = SearchSerializer(data=results, many=True)
#         serializer.is_valid()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

class SearchAPI(APIView):
    def get(self, request, slug):
        results = Searcher.searcher(slug)
        serializer = SearchSerializer(data=results, many=True)
        print(serializer.is_valid())
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, slug):
        name = request.data["name"]
        results = Searcher.searcher(name)
        serializer = SearchSerializer(data=results, many=True)
        print(serializer.is_valid())
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class DetailSearchAPI(APIView):
    def get(self, request, slug):
        info = Searcher.fa_search(slug)[0]
        dl = Searcher.base_extract(info)
        serializer = SearchSerializer(data=dl)
        print(serializer.is_valid())
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        name = request.data["name"]
        info = Searcher.fa_search(name)[0]
        dl = Searcher.base_extract(info)
        serializer = SearchSerializer(data=dl)
        print(serializer.is_valid())
        return Response(data=serializer.data, status=status.HTTP_200_OK)