license   = 'GPL v3'
copyright = '2024–25, Guide Version'
docformat = 'restructuredtext en'

from calibre.gui2.actions import InterfaceAction
from calibre.utils.date import format_date, now as calibre_now
from qt.core import QMessageBox
import traceback

class DatestampAndViewAction(InterfaceAction):
    name = 'Datestamp and View Action (Guide)'
    action_spec = (
        'Datestamp && View (Guide)', None,
        'Set #lastopened date and view book(s)', None
    )

    def location_pref(self):
        return 'toolbar, context-menu'

    def genesis(self):
        # Connect toolbar/menu button to our run_action
        self.qaction.triggered.connect(self.run_action)

    def run_action(self):
        lookup = '#lastopened'
        fmt    = 'iso'

        # 1. Get selected books
        book_ids = self.gui.library_view.get_selected_ids()
        if not book_ids:
            QMessageBox.warning(
                self.gui, 'No books selected',
                'Select one or more books first.'
            )
            return

        # 2. Verify custom column exists and is Date
        db = self.gui.current_db
        meta = db.field_metadata
        if lookup not in meta.custom_field_keys(False):
            QMessageBox.critical(
                self.gui, 'Missing column',
                f'Create the custom column {lookup!r} (type Date) first.'
            )
            return
        if meta[lookup]['datatype'] != 'datetime':
            QMessageBox.critical(
                self.gui, 'Wrong column type',
                f'Column {lookup!r} must be a Date column.'
            )
            return

        # 3. Build timestamp string
        stamp = format_date(calibre_now(), fmt)

        # 4. Write timestamp using the high-level API (works in Calibre 8)
        try:
            for bid in book_ids:
                # commit=True by default
                db.set_custom(bid, stamp, label=meta.key_to_label(lookup))
        except Exception:
            QMessageBox.critical(
                self.gui, 'Database error',
                f'Failed to set last-opened date:\n{traceback.format_exc()}'
            )
            return

        # 5. Refresh the library rows so you see the new date
        model = self.gui.library_view.model()
        model.refresh_ids(book_ids)
        self.gui.current_view().refresh_book_details()

        # 6. Open the book viewer via its QAction
        try:
            view_action = self.gui.iactions['View']
            view_action.qaction.trigger()
        except Exception:
            QMessageBox.critical(
                self.gui, 'Viewer error',
                f'Date set, but failed to open viewer.\n\n{traceback.format_exc()}'
            )
