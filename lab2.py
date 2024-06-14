def main():
    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name': "Cameron Benner",
        'student_id': 755373200406,
        'pizza_toppings': ['PEPPERONI', 'GREEN PEPPER', 'BACON'],  # Fix typo in 'GREEN PERPER'
        'movies': [
            {'title': "Real Steel", 'genre': 'Action'},
            {'title': 'Pacific Rim', 'genre': 'Sci-fi'}
        ]
    }

    # TODO: Step 3 - Add a new movie to the data structure
    new_movie = {'title': 'Inception', 'genre': 'Horror'}
    about_me['movies'].append(new_movie)

    # TODO: Step 4 - Function that prints student name and ID
    def print_student_name_and_id(about_me):
        full_name = about_me["full_name"]
        first_name = full_name.split()[0]
        student_id = about_me["student_id"]
        print(f"My name is {full_name}, but you can call me Sir {first_name}.\nMy student ID is {student_id}.")

    # TODO: Step 5 - Function that adds pizza toppings to data structure
    def add_pizza_toppings(about_me, toppings):
        about_me['pizza_toppings'].extend(toppings)
        about_me['pizza_toppings'].sort()
        about_me['pizza_toppings'] = [topping.lower() for topping in about_me['pizza_toppings']]

    # TODO: Step 6 - Function that prints bullet list of pizza toppings
    def print_pizza_toppings(about_me):
        print("My fav Pizza toppings are:")
        for topping in about_me['pizza_toppings']:
            print(f" - {topping}")

    # TODO: Step 7 - Function that prints movie genres
    def print_movie_genres(about_me):
        genres = [movie['genre'] for movie in about_me['movies']]
        print(f"I like to watch {genres[0]}, {genres[1]}, {genres[2]} movies.")
        
    # Fix index error
 

    def print_movie_titles(about_me):
        titles = [movie['title'].title() for movie in about_me['movies']]
        print(f"Some of my favourite movies are {', '.join(titles)}!")
    # Call the functions
    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me, ['MUSHROOM', 'SAUSAGE'])
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me)


if __name__ == '__main__':
    main()
