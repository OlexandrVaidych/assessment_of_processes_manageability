class ManageabilityProcessAssessment:
    def calculate_processes_manageability_assessments(self, a, b, projection_assessment):
        k1 = 2  # for regular mode
        k2 = 3 / 2  # for a critical situation
        k3 = 1 / 2  # for an accident

        assessment1 = round(1 - ((projection_assessment - a) / (b - a)) ** k1, 2)

        assessment2 = round(1 - ((projection_assessment - a) / (b - a)) ** k2, 2)

        assessment3 = round(1 - ((projection_assessment - a) / (b - a)) ** k3, 2)

        assessments = [assessment1, assessment2, assessment3]

        return assessments

    def calculate_projection_assessment(self, a, b, convolution):
        projection_assessment = convolution * (b - a) + a

        return projection_assessment

    def calculate_convolution(self, membership_functions, normalized_weight_coeffs):
        convolution = 0

        for i in range(len(membership_functions)):
            convolution += membership_functions[i] * normalized_weight_coeffs[i]

        return round(convolution, 3)

    def calculate_norm_weight_coeffs(self, weight_coeffs):
        norm_weight_coeffs = []
        sum_weight_coeffs = sum(weight_coeffs)

        for coeff in weight_coeffs:
            norm_weight_coeff = coeff / sum_weight_coeffs

            norm_weight_coeffs.append(round(norm_weight_coeff, 2))

        return norm_weight_coeffs

    def calculate_membership_function(self, evaluations, T1, T5):
        membership_functions = []

        for i in range(len(evaluations)):
            if (evaluations[i] > (T1[0] + T5[1]) / 2) & (evaluations[i] <= T5[1]):
                membership_function = 1 - 2 * ((T5[1] -evaluations[i]) / (T5[1] - T1[0])) ** 2
            else:
                membership_function = 2 * ((evaluations[i] - T1[0]) / (T5[1] - T1[0])) ** 2

            membership_functions.append(round(membership_function, 2))

        return membership_functions

    def evaluate_manageability_process(self, input_data, terms, weight_coeffs):
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

        normalized_weight_coeffs = self.calculate_norm_weight_coeffs(weight_coeffs)

        convolution = self.calculate_convolution(membership_functions, normalized_weight_coeffs)

        projection_assessment = self.calculate_projection_assessment(T1[0], T5[1], convolution)

        processes_manageability_assessments = self.calculate_processes_manageability_assessments(T1[0], T5[1],
                                                                                            projection_assessment)

        processes_manageability_assessments_str = f"Processes manageability assessments: \n"\
                                                  f"For regular mode - {processes_manageability_assessments[0]}\n"\
                                                  f"For a critical situation - {processes_manageability_assessments[1]}\n"\
                                                  f"For an accident - {processes_manageability_assessments[2]}"

        return processes_manageability_assessments_str
