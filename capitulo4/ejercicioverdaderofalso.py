can_fly='si'
is_human='si'
has_mask='si'

if can_fly=='si' and is_human=='si' and has_mask=='si':
    print("ironman")

if can_fly=='si' and is_human=='si' and has_mask=='no':
    print("ronan accuser")


if can_fly=='no' and is_human=='si' and has_mask=='si':
    print("spiderman")

if can_fly=='no' and is_human=='no' and has_mask=='si':
    print("black bolt")

if can_fly=='si' and is_human=='si' and has_mask=='no':
    print("captain marvel")

if can_fly=='si' and is_human=='no' and has_mask=='no':
    print("vision")

if can_fly=='no' and is_human=='si' and has_mask=='no':
    print("hulk")

if can_fly=='no' and is_human=='no' and has_mask=='no':
    print("thanos")