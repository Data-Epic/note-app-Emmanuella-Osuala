#A SmartNotesManager to help users create, organize,and manage different types of notes#
from datetime import datetime #import datetime class from datetime module#

class Note:
    """
    A Base class called Note.
    
    Attributes:
        content (str): The actual note text.
        created_at (datetime): Automatic Timestamp when the note was added.
    """
    def __init__(self, content):
        self.content = content
        self.created_at = datetime.now()  # Automatically set timestamp
    
    def display(self):
        """Display note details."""
        print(f"Note: {self.content}")
        print(f"Created at: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")

class TextNote(Note):
    """
    A specialized class representing a simple text-based note.
    """
    def display(self):
        """
        Display details of the text note.
        """
        print(f"Text Note: {self.content} (Created at: {self.created_at})")

class ReminderNote(Note):
    """
    A specialized note that includes an additional reminder date and time.
    
    """
    def __init__(self, content, reminder_time):
        """
        Initializes a new reminder note with content and reminder time.
        
        Args:
            content (str): The content of the note.
            reminder_time (str): The reminder time as a string (e.g., '2025-03-01 15:30').
        """
        super().__init__(content)
        self.reminder_time = reminder_time

    def display(self):
        """
        Display details of the reminder note.
        """
        print(f"Reminder Note: {self.content} (Created at: {self.created_at}, Reminder at: {self.reminder_time})")

class NotesManager:
    """
    A class to manage multiple notes.
    
    Attributes:
        notes (list): List to store notes.
        next_id (int): Counter for assigning unique IDs to notes.
    """
    def __init__(self):
        """
        Initializes the NotesManager with an empty list of notes and sets the initial note ID.
        """
        self.notes = []  #empty list
        self.next_id = 1  # Unique ID for each note

    def add_note(self, note_type, content, reminder_time=None):
        """
        Adds a new note of the specified type.
        
        Args:
            note_type (str): The type of note ('text' or 'reminder').
            content (str): The content of the note.
            reminder_time (str, optional): The reminder time, if applicable.
        """
        note = None
        if note_type.lower() == 'text':
            note = TextNote(content)
        elif note_type.lower() == 'reminder':
            note = ReminderNote(content, reminder_time)
        else:
            print("Invalid note type. Please choose 'text' or 'reminder'.")
            return

        # Assign a unique ID to the note for management purposes.
        note.id = self.next_id
        self.next_id += 1

        self.notes.append(note)
        print(f"Added {note_type} note with ID {note.id}.")

    def delete_note(self, note_id):
        """
        Deletes a note by its unique ID.
        
        Args:
            note_id (int): The unique ID of the note to delete.
        """
        for note in self.notes:
            if hasattr(note, 'id') and note.id == note_id:
                self.notes.remove(note)
                print(f"Deleted note with ID {note_id}.")
                return
        print("Note not found.")

    def show_notes(self):
        """
        Displays all stored notes.
        """
        if not self.notes:
            print("No notes to display.")
            return

        for note in self.notes:
            note.display()

    def search_notes(self, keyword):
        """
        Searches for and displays notes containing the specified keyword.
        
        Args:
            keyword (str): The keyword to search for in note contents.
        """
        found = False
        for note in self.notes:
            if keyword.lower() in note.content.lower():
                note.display()
                found = True
        if not found:
            print("No matching notes found.")
        
#main execution block
if __name__ == "__main__":
    my_notes = NotesManager()

    while True:
        print("\nThis is a Smart Notes Manager")
        print("Type 1 to Add Note")
        print("TYpe 2 to Show Notes")
        print("Type 3 to Search Notes")
        print("Type 4 to Delete Note")
        print("Type 5 to Exit Smart Notes Manager")
        choice = input("Enter your choice: ")

        if choice == "1":
            note_type = input("Enter note type (text/reminder): ").strip().lower()
            content = input("Enter note content: ")
            reminder_time = None
            if note_type == "reminder":
                reminder_time = input("Enter reminder time (YYYY-MM-DD HH:MM): ")

            my_notes.add_note(note_type, content, reminder_time)

        elif choice == "2":
            my_notes.show_notes()

        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            my_notes.search_notes(keyword)

        elif choice == "4":
            note_id = int(input("Enter note ID to delete: "))
            my_notes.delete_note(note_id)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")

