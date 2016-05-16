from django.shortcuts import render
import json

from django.core import serializers

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from django.views import generic

from .models import WorkPosition, RequiredSkills, CalculationResult, ResultDichotomy

app_name = 'dichotomy'


class IndexView(generic.ListView):
    template_name = 'dichotomy/index.html'
    context_object_name = 'test'

    def get_queryset(self):
        return ''


def get_workplaces(request, get_all):
    return HttpResponse(serializers.serialize('json', WorkPosition.objects.all()))


def get_workplace(request, id):
    work_position = WorkPosition.objects.get(pk=id)
    return HttpResponse(
        serializers.serialize('json',
                              list(WorkPosition.objects.filter(pk=id)) + list(work_position.requiredskills_set.all())))


def create_workplace(request):
    request_body_unicode = request.body.decode('utf-8')
    request_data = json.loads(request_body_unicode)
    work_position = WorkPosition(position_name=request_data['name'])
    work_position.save()
    required_skills = []
    for skill in request_data['skills']:
        required_skills.append(
            RequiredSkills(working_position_id=work_position, skill_name=skill['name'], rating=skill['rating']))
    RequiredSkills.objects.bulk_create(required_skills)
    return JsonResponse({'id': work_position.id, 'name': work_position.position_name})


def calculate_dichotomy(request):
    request_body_unicode = request.body.decode('utf-8')
    request_data = json.loads(request_body_unicode)
    generalizing_list = [item for item in request_data if item['poll'] == '1']
    detailing_list = [item for item in request_data if item['poll'] == '2']
    participant_list = [item for item in request_data if item['poll'] == '3']
    observer_list = [item for item in request_data if item['poll'] == '4']
    object_oriented_list = [item for item in request_data if item['poll'] == '5']
    connection_oriented_list = [item for item in request_data if item['poll'] == '6']
    indetifying_list = [item for item in request_data if item['poll'] == '7']
    resultant_list = [item for item in request_data if item['poll'] == '8']
    if len(generalizing_list) != 0:
        generalizing_avg = sum(item['fields']['rating'] for item in generalizing_list) / float(len(generalizing_list))
    else:
        generalizing_avg = 0

    if len(detailing_list) != 0:
        detailing_avg = sum(item['fields']['rating'] for item in detailing_list) / float(len(detailing_list))
    else:
        detailing_avg = 0

    if len(participant_list) != 0:
        participant_avg = sum(item['fields']['rating'] for item in participant_list) / float(len(participant_list))
    else:
        participant_avg = 0
    if len(observer_list) != 0:
        observer_avg = sum(item['fields']['rating'] for item in observer_list) / float(len(observer_list))
    else:
        observer_avg = 0
    if len(object_oriented_list) != 0:
        object_oriented_avg = sum(item['fields']['rating'] for item in object_oriented_list) / float(
            len(object_oriented_list))
    else:
        object_oriented_avg = 0
    if len(connection_oriented_list) != 0:
        connection_oriented_avg = sum(item['fields']['rating'] for item in connection_oriented_list) / float(
            len(connection_oriented_list))
    else:
        connection_oriented_avg = 0
    if len(indetifying_list) != 0:
        indetifying_avg = sum(item['fields']['rating'] for item in indetifying_list) / float(len(indetifying_list))
    else:
        indetifying_avg = 0
    if len(resultant_list) != 0:
        resultant_avg = sum(item['fields']['rating'] for item in resultant_list) / float(len(resultant_list))
    else:
        resultant_avg = 0
    poll1 = ''
    poll2 = ''
    poll3 = ''
    poll4 = ''
    if generalizing_avg > detailing_avg:
        poll1 = 'generalizing'
    elif generalizing_avg < detailing_avg:
        poll1 = 'detailing'
    if participant_avg > observer_avg:
        poll2 = 'participant'
    elif participant_avg < observer_avg:
        poll2 = 'observer'
    if object_oriented_avg > connection_oriented_avg:
        poll3 = 'object_oriented'
    elif indetifying_avg > resultant_avg:
        poll3 = 'indetifying'
    elif indetifying_avg < resultant_avg:
        poll4 = 'resultant'
    dichotomy_class_name = '<' + poll1 + '-' + poll2 + '|' + poll3 + '-' + poll4 + '>'
    result_dichotomy = ResultDichotomy(pole_1=poll1, pole_2=poll2, pole_3=poll3, pole_4=poll4,
                                       name=dichotomy_class_name)

    result_dichotomy.save()

    calculation_result = CalculationResult(generalizing=generalizing_avg, detailing=detailing_avg,
                                           participant=participant_avg,
                                           observer=observer_avg, object_oriented=object_oriented_avg,
                                           connection_oriented=connection_oriented_avg, identifying=indetifying_avg,
                                           resultant=resultant_avg,
                                           working_position_id_id=request.POST.get('workplace_id'),
                                           result_dichotomy_id_id=result_dichotomy)
    calculation_result.save()
