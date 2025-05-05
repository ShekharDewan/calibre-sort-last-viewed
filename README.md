# Datestamp and View (Guide) Calibre Plugin

A Calibre “InterfaceAction” plugin that, in a single click, sets a custom “Last Opened” (`#lastopened`) date/time on selected book(s) and immediately opens them in Calibre’s built-in viewer.

---

## Features

- Records the current date/time into a user-defined custom column `#lastopened` (type Date)  
- Opens selected book(s) in Calibre’s default viewer  
- No external dependencies—uses Calibre’s public plugin APIs  
- Works on Calibre 5.0+ (tested through Calibre 8.0.1) on Windows, macOS, and Linux  

---

## Repository Structure


datestamp\_view\_guide/
├── init.py
├── action.py
├── plugin-import-name-datestamp\_view\_guide.txt   ← (empty file)
└── README.md


- **init.py**  
  Defines the plugin metadata and points Calibre to the GUI logic class.

- **action.py**  
  Implements the `DatestampAndViewAction` class:  
  1. Validates selection and custom column  
  2. Writes the timestamp via Calibre’s API  
  3. Refreshes the library view  
  4. Triggers Calibre’s viewer action  

- **plugin-import-name-datestamp_view_guide.txt**  
  Must be present (empty) to define the Calibre plugin namespace  
  `calibre_plugins.datestamp_view_guide`.

---

## Installation

1. **Create the `#lastopened` column**  
   In Calibre’s main window, go to **Preferences → Add your own columns**.  
   - Lookup name: `#lastopened`  
   - Column heading: e.g. “Last Opened”  
   - Type: **Date**

2. **Package the plugin**  
   From the repository root, create a ZIP archive containing exactly the three files at its root (no parent folder):
   ```bash
   zip -j datestamp_view_guide-3.0.9.zip init.py action.py plugin-import-name-datestamp_view_guide.txt

3. **Load into Calibre**

   * Open **Preferences → Plugins → Load plugin from file…**
   * Select `datestamp_view_guide-3.0.9.zip`
   * Restart Calibre if prompted.

4. **Enable the action**

   * Go to **Preferences → Toolbars and menus → Customize toolbars/menus**
   * Under “Available actions,” find **Datestamp && View (Guide)** and add it to your toolbar or context menu.
   * Click **Apply** and close.

---

## Usage

1. Select one or more books in your Calibre library view.
2. Click the **Datestamp && View** button (or use its context-menu entry).
3. The plugin will:

   * Update the **Last Opened** column with the current ISO date/time.
   * Immediately open the selected book(s) in Calibre’s viewer.

---

## Development & Testing

* **Calibre version**: 8.0.1
* **Python**: Embedded 3.11.5
* **Platforms**: macOS 15.3.2 (ARM64), Windows, Linux

To iterate on the plugin, modify `action.py` or `init.py`, re-zip, then reload via Calibre’s plugin interface.

---

## Contributing

1. Fork this repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes and push: `git push origin feature-name`
4. Open a pull request describing your improvements.

---

## License

This project is licensed under the [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html). See **init.py** for full license notice.
