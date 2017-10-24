from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from django.db import models
from quiz.models import Question

from django.views.generic.detail import DetailView



class Int_Question(Question):
    correct = models.IntegerField(blank=False,
                                  default=False,
                                  help_text=_("Answer must be an integer number"
                                              ),
                                  verbose_name=_("Correct"))

    def check_if_correct(self, guess):
        if guess == self.correct:
            return True
        else:
            return False

    def get_answers(self):
        return False

    def get_answers_list(self):
        return False

    def answer_choice_to_string(self, guess):
        return str(guess)

    class Meta:
        verbose_name = _("Integer Question")
        verbose_name_plural = _("Integer Questions")
        ordering = ['category','sub_category']
