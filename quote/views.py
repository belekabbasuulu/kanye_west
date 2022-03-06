from rest_framework.views import APIView
from rest_framework.response import Response
from collections import Counter
import requests
import json

from .serializers import QuoteSerializer
from .models import Quote


def without_sym(text):
    k = ''
    for i in text:
        if i.isalpha() or i==' ' or i=="'" or i=="-":
            k = k + i
    return k
    
class QuoteAPIViewSet(APIView):
    def get(self, request):
        objs = []
        for i in range(10):
            response = requests.get('https://api.kanye.rest')
            response = json.loads(response.text)
            quote = without_sym(response['quote'])
            str_sort = sorted(without_sym(quote).split(), key=len)[:-4:-1]
            n = len(str_sort)
            alph = [i for i in quote if i.isalpha()]
            text = ''.join(alph)
            counter = dict(Counter(text))
            instance, created = Quote.objects.get_or_create(quote=quote,
                defaults={
                    'num_letters': len(alph), 
                    'num_vowels': sum(1 for b in quote if b in 'aeiou'),
                    'num_consonants': sum(1 for b in quote if b.isalpha() and b not in 'aeiou'),
                    'num_repetition': counter,
                    'average': sum(len(i) for i in quote.split()) / len(quote.split()),
                    'long_word_1': str_sort[0] if n > 0 else '',
                    'long_word_2': str_sort[1] if n > 1 else '',
                    'long_word_3': str_sort[2] if n > 2 else ''
                }    
            )
            objs.append(instance)
        serializer = QuoteSerializer(objs, many=True)
        return Response(serializer.data)




