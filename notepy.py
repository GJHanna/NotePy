from argparse import ArgumentParser
from sys import argv
from os import chdir, getcwd, path
from subprocess import Popen

parser = ArgumentParser(description='NotePy verion 1.0')
parser.add_argument('create', nargs='+', help='create .notes.txt file')
parser.add_argument('-l', '--list', action='store_true', help='list notes')
parser.add_argument('-a', '--append', action='store_true', help='append new note')
parser.add_argument('-r', '--remove', action='store_true', help='remove note')

class PrettyPrint(object):

    @staticmethod
    def purple(msg):
        print('\033[95m' + msg + '\033[0m')

    @staticmethod
    def blue(msg):
        print('\033[94m' + msg + '\033[0m')
    
    @staticmethod
    def green(msg):
        print('\033[92m' + msg + '\033[0m')
    
    @staticmethod
    def warning(msg):
        print('\033[93m' + msg + '\033[0m')
    
    @staticmethod
    def fail(msg):
        print('\033[91m' + msg + '\033[0m')

def init_notes(wdir):
    try:
        Popen('touch .notes.txt', shell=True)
        PrettyPrint.green('Successfully created .notes.text file in {}'.format(wdir))
    except OSError as err:
        print(err)
        PrettyPrint.fail('Failed to create .notes.txt file')

def append_note(note):
    try:
        with open('.notes.txt', 'a') as file:
            file.write(note + '\n')
    except OSError as err:
        print(err)
        PrettyPrint.fail('Failed to append note')
    except Exception as err:
        PrettyPrint.warning(
'''
Insert your note between quotations
Example:
Note to append: "This is my note"
''')

def remove_note(wdir):
    list_notes(wdir)
    try:
        if (path.getsize('.notes.txt')):
            i = int(input('Enter the number of note you want to delete between quotaions: '))
            with open('.notes.txt', 'r') as file:
                notes = file.readlines()
            del notes[i - 1]
            with open('.notes.txt', 'w+') as file:
                [file.write(note) for note in notes]
                
    except OSError as err:
        print(err)
        PrettyPrint.fail('Failed to append note')
    except IndexError:
        PrettyPrint.fail("Number of note chosen is doesn't exist")
    except ValueError:
        PrettyPrint.fail('''
Make sure you insert an integer 
Example:
Enter the number of note you want to delete between quotaions: "1"
''')
    except Exception as err:
        PrettyPrint.warning(
'''
Insert the note number between quotations
Example:
Enter the number of note you want to delete between quotaions: "1"
''')

def list_notes(wdir):
    try:
        if (path.getsize('.notes.txt')):
            with open('.notes.txt', 'r') as file:
                PrettyPrint.blue('The notes for {} are: '.format(wdir))
                for i, note in enumerate(file):                
                    print(str(i + 1) + '- ' + note)
        else:
            PrettyPrint.warning('No notes exist for {}'.format(wdir))
    except OSError as err:
        print(err)
        PrettyPrint.fail('Failed to append note')
    except Exception as err:
        print(err)

def main():
    args = vars(parser.parse_args())
    wdir = args['create'][0]
    chdir(wdir) 

    if(len(args['create']) > 1):
        if (args['create'][1] == 'init'):
            try:
                if (not path.isfile(wdir + '/.notes.txt')):
                    init_notes(wdir)
                else:
                    PrettyPrint.warning("File '.notes.txt' already exists")
            except OSError as err:
               print(err)

    if (args['list']):
        list_notes(wdir)

    if (args['append']):        
        append_note(input('Note to append: '))

    if (args['remove']):
        remove_note(wdir)

if __name__ == "__main__":
    main()
    exit()