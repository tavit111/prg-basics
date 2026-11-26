import queue

# tworzymy pustą kolejkę kto pierwszy przyszedł ten pierwszy obsłużony
customers = queue.Queue()

# zaczynamy numerowanie biletów od 1
ticket_number = 1

# pętla działa w kółko dopóki nie wpiszemy 0
while True:
    print("1. New customer")
    print("2. Serve customer")
    print("0. Exit")
    choice = input("Select an option: ").strip()

    # dodajemy nowego klienta na koniec kolejki z kolejnym numerem
    if choice == '1':
        customers.put(ticket_number)
        print(f"Customer with ticket #{ticket_number} added to the queue")
        # zwiększamy numer biletu o 1 dla następnej osoby
        ticket_number += 1

    # obsługujemy pierwszego klienta z początku kolejki
    elif choice == '2':
        # sprawdzamy czy kolejka nie jest pusta
        if not customers.empty():
            # bierzemy pierwszą osobę z przodu kolejki
            served_customer = customers.get()
            print(f"Serving customer with ticket #{served_customer}")
        else:
            print("Queue is empty")

    # przerywamy pętlę i kończymy program
    elif choice == '0':
        break

    else:
        print("Invalid option")

    print()