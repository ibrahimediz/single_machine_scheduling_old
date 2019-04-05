# single_machine_scheduling
In make-to-order manufacturing environments, scheduling is usually referred to as a customer order scheduling (COS)where the problem is to satisfy the demand of several customers, who give orders with a set of products (jobs), and all jobs in a customer order are packed and delivered to the customer when the processing of all the jobs in that customer order is completed. Thus, the completion time of the job processed as the last job in a customer order is also the completion time of that customer order. 

There are two extreme approaches for producing the products: (1) the order-based processing, and (2) the job-based processing. In the COS problem with order-based processing, all jobs (products) in a customer order are processed successively without intermingled with jobs of other customer orders. However, same jobs from different customer orders are processed together in the COS problem with job-based processing. It is clear that the objective function values of the COS problems with these two extreme processing approaches are expected to be different. The optimal solution of the COS problem with order-based processing is easy and polynomial-time solvable [1] when the scheduling objective is to minimize the total completion time, which is the sum of the completion times of the customer orders and equivalent to minimizing total work-in-process inventory focusing on increasing the customer satisfaction. However, the COS problem with job-based processing with the same scheduling objective is not easy as the order-based processing. In the job-based processing, there are two questions that must be answered simultaneously: (1) what will be the processing sequence of the jobs, and (2) what will be the processing sequence of the customer orders in each job, so that the scheduling objective is minimized.

In this thesis, we will investigate the COS problem with order-based and job-based processing approaches where jobs are produced on a single manufacturing facility (machine) to minimize the total completion time. We will first identify the basic properties of the optimal solution for the COS problem with job-based processing, develop different mixed integer programming (MILP) models to solve this COS problem optimally, and then compare the MILP models based on the size complexity. Furthermore, we will develop metaheuristic heuristic algorithm(s) to for large scale problems in which a solution cannot be obtained by the MILP model. The optimization software package GAMS will be used for solving MILP models. Computational experiments will be done to evaluate the performance of our solution approaches in terms of both solution quality and computational time, and to compare the order-based and job-based processing approaches, based on the objective function value.
