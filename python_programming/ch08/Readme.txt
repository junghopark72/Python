1. Function

   - Function Name (mandatory)

   - Argument (optional)

   - Return Value (optional)
     : return None ('NoneType')

   - Default Argument Value
     A) def <func_name>(<arg_name>=<default_value>)
     B) 'None' argument

   - Keywork Arguments

     def introduce_my_car(manufacturer, seats=4, type='sedan):

     A) introduce_my_car()
     	-> TypeError: introduce_my_car() missing 1 required positional argment: 'XXX'

     B) introduce_my_car(manufacturer='Hyundai', 2)
     	-> SyntaxError: non-keyword arg after keyword arg

     C) introduce_my_car('Kia', manufacturer='Hyundai')
     	-> TypeError: introduce_my_car() got multiple values for argument 'manufacturer'

     D) introduce_my_car(color='Gray')
     	-> TypeError: introduce_my_car() got an unexpected keyword argument 'color'

   - Arbitrary Argument Lists
     A) * -> Tuple data input
     B) ** -> Dictionary data input

2. Class


3. Module
