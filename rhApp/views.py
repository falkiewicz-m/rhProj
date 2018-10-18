from django.shortcuts import render
from .forms import rhSurvey1
from django.forms.formsets import formset_factory
from .models import QuestionM, ChoiceM
# Create your views here.



def survey(request):
    if request.method == 'POST':
        form1 = rhSurvey1(request.POST)
        # form2 = rhSurvey2(request.POST)
        if form1.is_valid():




            message = 'All looks fine now'


            for fnum, item in enumerate(form1.fields, start=1):

                str_a = 'answers_' + str(fnum)
                choice_str_a = form1.cleaned_data[str_a]
                g = ChoiceM.objects.get(question_fk = fnum, choice_text = choice_str_a)
                g.numberOfVotes += 1
                g.save()





            return render(request, 'rhApp/ankieta.html', {'form1': form1, 'message' : message })

    elif request.method == 'GET':
        message = 'it was get you know'

        form1 = rhSurvey1()
        # form2 = rhSurvey2()
        return render(request, 'rhApp/ankieta.html', {'form1': form1, 'message' : message })

def excludeCSRF(dict, csrft):
    return {k:v for k,v in dict if k not in csfrt}
# def save(self, commit=True):
#     instance = super(rhSurvey1, self).save(commit=False)
#
#
# def vote(request, question_fk_id):
#     quest = get_object_or_404(QuestionM, pk=question_fk_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice_'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.numberOfVotes += 1
#         selected_choice.save()
