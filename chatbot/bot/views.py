from django.shortcuts import render
from django.http import JsonResponse
import openai
# Create your views here.

openai_key= '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'
openai.api_key=openai_key
def openAi(message):
    response=openai.ChatCompletion.create(
        model='text-davinci-003',
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    print(response)
    answer = response.choices[0].message.content.strip()
    return answer

def chatbotview(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        #response = openAi(message)
        response="I AM FINE"
        return JsonResponse({'message': message, 'response': response})
    return render(request,'chatbot.html')