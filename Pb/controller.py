import view
import model
import text_fields as txt


def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(txt.load_successful)

            case 2:
                model.save_file()
                view.print_info(txt.save_successful)

            case 3:
                pb = model.get_pb()
                view.show_contact(pb, txt.no_contacts_or_file)

            case 4:
                contact = view.new_contact()
                model.add_contact(contact)
                view.print_info(txt.new_contact_successful)

            case 5:
                find_data = view.input_find_contact()
                successful_find = model.find_in_phone_book(find_data)
                if successful_find:
                    view.print_find_contact(successful_find)
                else:
                    view.print_info(txt.find_error)

            case 6:
                pb = model.get_pb()
                view.show_contact(pb, txt.no_contacts_or_file)
                point = view.print_change_contact()
                find_contact = model.find_for_change_phone_book(point)
                change_point = view.change_contact(find_contact)
                model.change_phone_book(change_point, point)
                view.print_info(txt.changed_successful)

            case 7:
                pb = model.get_pb()
                view.show_contact(pb, txt.no_contacts_or_file)
                point = view.print_del_contact()
                model.del_phone_book(point)
                view.print_info(txt.del_successful)
            case 8:
                if model.exit_pb():
                    if view.confirm(txt.is_changed):
                        model.save_file()
                view.print_info(txt.bye_bye)
                break
