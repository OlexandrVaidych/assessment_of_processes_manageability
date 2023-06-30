class ManageabilityProcessAssessment:

    def evaluate_manageability_process(self, input_data, terms):
        T1 = [0, 20]
        T2 = [20, 40]
        T3 = [40, 60]
        T4 = [60, 80]
        T5 = [80, 100]

        criterion_evaluation1 = input_data[0] * T4[1]

        criterion_evaluation2 = input_data[1] * T5[1]

        criterion_evaluation3 = input_data[2] * T5[1]

        criterion_evaluation4 = input_data[3] * T5[1]

        criterion_evaluation5 = input_data[4] * T3[1]

        criterion_evaluations = [criterion_evaluation1, criterion_evaluation2, criterion_evaluation3,
                                 criterion_evaluation4, criterion_evaluation5]
