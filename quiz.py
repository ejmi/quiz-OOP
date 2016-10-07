from questions.questions import questions
import random

class Questions(object):
    questions = []

    def __init__(self):
        self.questions = questions

    def getQuestion(self):
        index = random.randint(0, len(self.questions)-1)
        question = self.questions.pop(index)
        return question

    def printQuestion(self, q):
        print "Here's a question:\n"
        print "\t {}".format(q['question']) 

    def printAnswer(self, q):
        print "\t\ta. %-25s b. %s" % (q['answers']['a'],q['answers']['b'])
        print "\t\tc. %-25s d. %s" % (q['answers']['c'],q['answers']['d'])
  
    def questions_count(self):
        return len(self.questions)




#
def get_answer(question):
    possible_answers = question['answers'].keys();
    player_answer = raw_input("Your answer: ").lower()
    while player_answer not in possible_answers:
        print 'Choose: %s' % ','.join(possible_answers)
        quiz.printQuestion(question)
        quiz.printAnswer(question)
        player_answer = raw_input("Your answer: ").lower()
    return player_answer


if __name__ == "__main__":
    quiz = Questions()

    score = 0
    while quiz.questions_count() > 0:
        question = quiz.getQuestion()
        quiz.printQuestion(question)
        quiz.printAnswer(question)

        player_answer = get_answer(question)
        if player_answer == question['correct']:
            print "Correct! You get a score!"     
            score += 1     
            continue       
        else:         
            print "Unfortunately, correct answer is %s. You lost." % (question['correct'].upper())        
            print 'The end. Your score is: ', score       
            break  
              
        if score == quiz.questions_count():
            print 'Congratulations! You answered all the questions. Your score is: ', score
        else: 
            print 'The end. Your score is: ', score