
import random

dict_answers_survey = {
    'ranges':{
        'More_ranges':['Up to {}', 'More than {}'],
        'Less_range':['Less than {}', 'Down to {}'],
        'Between_range':['Between {} and {}']
    },
    'yes/no':{
        'Affirmative':['Yes', 'True', 'Correct'],
        'Negative':['No', 'False', 'Incorrect']

    },
    'time_freq':{
        'Frequency':['Once a {}', 'Twice a {}',
                    'Several times a {}', 'A few times per {}',
                    'All the {}'],
        'Time_particle':['year', 'week', 'day'],
        'Frequency_without_time':['Daily', 'Sometimes', 'Never',
                                'Always']
    },
    'quantif':{
        'Sup_quantif':['Higher {}', 'Superior {}'],
        'Inf_quantif':['Inferior {}', 'Primary {}']
    },
    'words':['Education','Income', 'Salary', 'Cholesterol',
                'Coke', 'Nutrients', 'Plants']
}

def create_fake_survey(number_people, number_questions, route_survey):
    surv_file = open(route_survey, 'w')

    # Compose the row format
    row_format              = [random.randrange(4) for i in range(number_questions)] 
    words_selection         = [random.randrange(len(dict_answers_survey)) for i in range(row_format.count(3))]
    true_false_selection    = [random.randrange(3) for i in range(row_format.count(1))]
    time_freq_selection     = [random.randrange(2) for i in range(row_format.count(2))]

    numbers_selection   = []

    for occ in range(row_format.count(0)):
        number_1 = random.randint(1,60000)
        number_2 = random.randint(number_1, number_1*1000)
        number_3 = random.randint(number_2, number_2*1000)
        
        numbers_selection.append([number_1, number_2, number_3])

    for q in range(number_questions):
        if q == 0:
            surv_file.write('Question_0')
        else:
            surv_file.write(',Question_{}'.format(q))

    surv_file.write('\n')

    for i in range(number_people):
        row = "{}".format(i)

        number_answer_index = 0
        word_answer_index   = 0
        true_false_index    = 0
        time_freq_index     = 0

        for j in range(number_questions):
            if row_format[j] == 0:
                kind_answer = random.randint(0,2)
                question = "{}".format(random.choice(dict_answers_survey['ranges'][list(dict_answers_survey['ranges'].keys())[kind_answer]]))
                
                if kind_answer == 2:
                    question = question.format(numbers_selection[number_answer_index][1],
                                        numbers_selection[number_answer_index][2])
                elif kind_answer == 1:
                    question = question.format(numbers_selection[number_answer_index][0])
                
                elif kind_answer == 0:
                    question = question.format(numbers_selection[number_answer_index][2])

                number_answer_index += 1

            elif row_format[j] == 1:
                kind_answer = random.randint(0,1)

                if kind_answer == 0:
                    question = "{}".format(dict_answers_survey['yes/no']['Negative'][true_false_selection[true_false_index]])
                
                elif kind_answer == 1:
                    question = "{}".format(dict_answers_survey['yes/no']['Affirmative'][true_false_selection[true_false_index]])
                
                true_false_index += 1

            elif row_format[j] == 2:
                kind_answer = time_freq_selection[time_freq_index]
                
                if kind_answer == 1:
                    question = "{}".format(random.choice(dict_answers_survey['time_freq']['Frequency_without_time']))

                elif kind_answer == 0:
                    question = "{}".format(random.choice(dict_answers_survey['time_freq']['Frequency']))
                    question = question.format(random.choice(dict_answers_survey['time_freq']['Time_particle']))
                
                time_freq_index += 1

            elif row_format[j] == 3:
                question = "{}".format(random.choice(dict_answers_survey['quantif'][random.choice(['Sup_quantif', 'Inf_quantif'])]))
                question = question.format(dict_answers_survey['words'][words_selection[word_answer_index]])
                
                word_answer_index += 1
            
            print(question)

            row += ",{}".format(question)

        surv_file.write("{}\n".format(row))