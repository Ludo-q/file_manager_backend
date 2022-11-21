import os
import shutil

# Create your views here.
from django.http import HttpResponse
from django.template import loader

folder_name_destination = 'lista_fundit'
base_url_destination = 'D:/{}'.format(folder_name_destination)

base_url_source_all1 = 'D:/1. Pjesa e pare'
base_url_source_all2 = 'D:/2. Pjesa e dyte'
base_url_source_all3 = 'D:/3. Pjesa e trete'

base_url_source = 'C:/Users/Biku/Desktop/FotoSkan/ne perpunim/1. perfunduar'

global_error_list = []

data = {
    'url': {
        'destination_folder': {
            'book_pdf': '{}/pdf_book'.format(base_url_destination),
            'book_word': '{}/word_book'.format(base_url_destination),
            'book_imgs': '{}/img_book'.format(base_url_destination),
            'cop_front_pdf': '{}/pdf_cover/front'.format(base_url_destination),
            'cop_back_pdf': '{}/pdf_cover/back'.format(base_url_destination),
            'cop_front_img': '{}/img_cover/front'.format(base_url_destination),
            'cop_back_img': '{}/img_cover/back'.format(base_url_destination),
        },
        'source_folder': {
            'all_book_pdf_part1': '{}/library/pdf_book'.format(base_url_source_all1),
            'all_book_pdf_part2': '{}/library/pdf_book'.format(base_url_source_all2),
            'all_book_pdf_part3': '{}/library/pdf_book'.format(base_url_source_all3),
        }
    },
    'file': {
        'pdf': 'pdf',
        'word': 'docx',
        'img': 'jpg'
    },
    'prefix': {
        'cover': 'cop_',
        'cover_back': 'cop_back',
    }
}


def index(request):
    destination_book_pdf_url = data['url']['destination_folder']['book_pdf']
    destination_book_word_url = data['url']['destination_folder']['book_word']
    destination_book_imgs_url = data['url']['destination_folder']['book_imgs']

    # context = {
    #     'app_title': 'Menaxho librat e skanuar',
    #     'option_name': 'Differenca ndermjet folderave: "PDF" VS "WORD"',
    #     'option_description':
    #         'Emrat e librave qe ndodhen ne folder',
    #     'files': get_all_files_from_folder(base_url_destination)
    # }

    # context = {
    #     'app_title': 'Menaxho librat e skanuar',
    #     'option_name': 'Krijo folderat distinacion',
    #     'files': create_destination_folders(),
    #     'errors': global_error_list
    # }

    global_error_list.clear()

    # 7. Confessioni
    # 8. Scrutate
    # 9. Il dolore nella Bibbia
    # 10. Genitori oggi
    # 11. Ogni giorno la sua gioia
    # 12. La spiritualità di Francesco d'Assisi
    # 13. A un passo dalla gioia!
    # 14. Il giorno della civetta
    # 15. La fede dal principio
    # 16. Parabole
    # 17. Giampiero Fabbretti
    # 18. La era dei martiri
    # 19. Maestro, insegnaci a pregare
    # 20. Mediterraneo senza frontiere
    # 21. Lettura pastoriale degli atti degli apostoli
    # 22. Il vangelo di Matteo
    # 23. Una comunità legge il Vangelo di Matteo
    # 24. Una comunità legge il Vangelo di Giovanni
    # 25. Una comunità legge il Vangelo di Marco
    # 26. Battezzati per diventare cristiani
    # 27. Il tipo ideale di vescovo secondo la riforma cattolica
    # 28. La Cresima
    # 29. I dolori mentali di Gesù nella sua Passione e autobiografia
    # 30. E celibato
    # 31. Vagliate ogni cosa, trattenete ciò che è buono
    # 32. Gesù pane di vita
    # 33. Itinerario della mente in Dio
    # 34. Cerchi nell'acqua
    # 35. L'importante è la rosa
    # 36. Solo il vento lo sa
    # 37. Il segreto dei pesci rossi
    # 38. Francesco e la parola
    # 39. Francisco de Asis y el Sultàn
    # 40. Abbecedario biblico
    # 41. Schede per leggere e approfondire le Costituzioni Generali OFM
    # 42. Formazione Vol. I
    # 43. Una forma di vita secondo il Vangelo
    # 44. Le davozioni materiali
    # 45. San Francesco e i suoi ordini
    # 46. De sponsalibus & Matrimonio tractatus canonicus & theologicus
    # 47. Jeta e shuguruar
    # 48. Vlere shpirterore
    # 49. Oso Kuka
    # 50.

    book_title_key = 'Bardha e Temalit'

    context = {
        'app_title': 'Menaxho librat e skanuar',
        'option_name': 'Duke kerkuar per librin: "{}"'.format(book_title_key),
        'files': check_if_book_exists(book_title_key),
        'errors': global_error_list
    }

    template = loader.get_template('manage_scanned_file/index.html')
    return HttpResponse(template.render(context, request))


def create_destination_folders():
    """
    Create 'lista_fundit' folder if not exists
    and
    all necessary sub folders if not exists.
    :return: A list of created sub folders
    """
    try:
        os.chdir(base_url_destination)
        error_list = []
        result_list = []
        for url in data['url']['destination_folder']:
            try:
                os.mkdir('{}/{}'.format(base_url_destination, url))
                result_list.append('Folderi me url: "{}" u krijua'.format(url))
            except FileExistsError:
                error_list.append('Folderi me url: "{}" ekziston tashme'.format(url))

        handle_errors(error_list)

        return result_list

    except FileNotFoundError:
        temp_base_url_destination = base_url_destination.replace(folder_name_destination, '')
        os.chdir(temp_base_url_destination)
        os.mkdir('{}{}'.format(temp_base_url_destination, folder_name_destination))

        handle_errors(['Folderi nuk u gjet. Nje folder i ri u krijua ne folderin: {}, me emer: {}'.format(
            temp_base_url_destination, folder_name_destination
        )])


def copy_books_to_default_destination(dst_base_path, file_extension, prefix=''):
    # Go to the source
    os.chdir(base_url_destination)
    dirs_files_list = os.listdir()

    for file in dirs_files_list:
        temp_file = prefix + file
        src = '{}/{}/{}.{}'.format(base_url_destination, file, temp_file, file_extension)
        dst = '{}/{}.{}'.format(dst_base_path, temp_file, file_extension)
        shutil.copy(src, dst)

    os.chdir(dst_base_path)

    return os.listdir()


def get_different_file_from_to_folder(folder_pdf, folder_word):
    os.chdir(folder_pdf)
    folder_pdf_files = os.listdir()
    os.chdir(folder_word)
    folder_word_files = os.listdir()

    diff_files_name = []

    for file in folder_pdf_files:
        temp_file = file.replace('.pdf', '.docx')
        if temp_file not in folder_word_files:
            diff_files_name.append(file)

    for file in folder_word_files:
        temp_file = file.replace('.docx', '.pdf')
        if temp_file not in folder_pdf_files:
            diff_files_name.append(file)

    return diff_files_name


def get_all_files_from_folder(folder_path):
    os.chdir(folder_path)
    return os.listdir()


def handle_errors(error_list):
    global_error_list.clear()
    for err in error_list:
        global_error_list.append(err)


def check_if_book_exists(title):
    temp_title = title.lower()
    all_books = []
    result_books = []
    # (word not in exception_books) add this as a condition when you have to much results
    exception_words = ['nella', 'della', 'atti']

    os.chdir(data['url']['source_folder']['all_book_pdf_part1'])
    for file in os.listdir():
        all_books.append(file)

    os.chdir(data['url']['source_folder']['all_book_pdf_part2'])
    for file in os.listdir():
        all_books.append(file)

    os.chdir(data['url']['source_folder']['all_book_pdf_part2'])
    for file in os.listdir():
        all_books.append(file)

    for book in all_books:
        temp_book = book.lower()
        words = temp_title.split(' ')

        for word in words:
            if (word in temp_book) and (len(word) > 3) and (book not in result_books) and (word not in exception_words):
                result_books.append(book)

    print(result_books)
    return result_books
