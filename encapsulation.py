class Employee:
    def __init__(self, name, salary, project):
        self.name = name          # Public: accessible anywhere
        self._project = project    # Protected: internal use / subclasses
        self.__salary = salary    # Private: hidden outside this class

    # Public method
    def show_details(self):
        # Internal access works for all three types
        return f"{self.name} works on {self._project} and earns {self.__salary}"

# --- Testing Access Outside the Class ---
emp = Employee("Alice", 85000, "Apollo")


# 1. Public Access
print(emp.name)          # Output: Alice

# 2. Protected Access
print(emp._project)      # Output: Apollo (Works, but IDEs will throw a warning)

# 3. Privayeete Access
print(emp._Employee__salary)    
