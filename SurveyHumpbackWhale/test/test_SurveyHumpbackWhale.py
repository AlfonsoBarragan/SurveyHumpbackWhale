import pytest
import pandas as pd

import SurveyHumpbackWhale.SurveyHumpbackWhale

@pytest.fixture()
def setup_survey():
    
    survey_dataset  = pd.read_csv( "test/datasets_to_test/fake_surv.csv")
    survey_dict     = SurveyHumpbackWhale.map_answers_to_categories(survey_dataset)

    def fin():
        survey_dataset  = []
        survey_dict     = {}

    request.addfinalizer(fin)

def test_correct_time_freq_adverb(setup_survey):
    daily_freq  = survey_dict['Question_1']['Daily'] 
    never_freq  = survey_dict['Question_1']['Never']
    some_freq   = survey_dict['Question_1']['Sometimes']
    alway_freq  = survey_dict['Question_1']['Always'] 
    
    assert  daily_freq > never_freq and daily_freq > some_freq and daily_freq <= alway_freq 
    
    assert  never_freq < daily_freq and never_freq < some_freq and never_freq < alway_freq 
    
    assert  some_freq > never_freq and some_freq < daily_freq and some_freq < alway_freq
             

