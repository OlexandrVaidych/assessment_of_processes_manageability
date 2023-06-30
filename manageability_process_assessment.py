class ManageabilityProcessAssessment:

    def calculate_membership_function(self, evaluations, T1, T5):
        membership_functions = []

        for i in range(len(evaluations)):
            if (evaluations[i] > (T1[0] + T5[1]) / 2) & (evaluations[i] <= T5[1]):
                membership_function = 1 - 2 * ((T5[1] -evaluations[i]) / (T5[1] - T1[0])) ** 2
            else:
                membership_function = 2 * ((evaluations[i] - T1[0]) / (T5[1] - T1[0])) ** 2

            membership_functions.append(round(membership_function, 2))

        return membership_functions

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

        membership_functions = self.calculate_membership_function(criterion_evaluations, T1, T5)

