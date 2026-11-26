# zmienne z danymi o filmie
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

# nazwa pliku, do ktorego zapisujemy dane
file_name = 'movie_details.txt'

# otwieram plik w trybie zapisu ('w') i wpisuje kolejne linijki tekstu
with open(file_name, 'w') as file:
    file.write(f"Movie Title: {movie_title}\n")
    file.write(f"Director: {director}\n")
    file.write(f"Lead Actor: {lead_actor}\n")

# potwierdzenie w terminalu, ze zapis sie udal
print(f"Movie details have been written to {file_name}.")