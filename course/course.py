"""
Description: Course Class.  
Author: Elusiyan Mathew Eluwole
"""
from department.department import Department

class Course:
    """
    Course class:  Maintains course data.
    Attributes:
        __name (str): The name of the course.
        __department (Department):  The department to which the course belongs.
        __credit_hours (int): The number of credit hours assigned to the course.

    Methods:
        __init__():  Initializes a course object.
        name(): Accessor for name attribute.
        department():  Accessor for department attribute.
        credit_hours(): Accessor for credit hours attribute.    
    """
    def __init__(self, name: str, department:Department, credit_hours: int):
        """
        Initializes the class attributes with argument values.
        Args:
            name (str): The name of the course.
            department (Department):  The department to which the course belongs.
            credit_hours (int): The number of credit hours assigned to the course.
        Raises:
            ValueError:
                When name is blank.
                When department is invalid.
                When credit hours is non-numeric.
        """
        if len(name.strip()) == 0:
            raise ValueError("Name cannot be blank.")
        else:
            # private attributes have a __ prefix.
            self.__name = name

        if isinstance(department, Department):
            self.__department = department
        else:
            # the type-hinting of the method causes
            # this to display in a lighter font.
            raise ValueError("Department is invalid.")
            
        if isinstance(credit_hours, int):
            self.__credit_hours = credit_hours
        else:
            raise ValueError("Credit hours must be numeric.")


            