# WhatsApp_Integrated_File_Watcher
This is the source code of WhatsApp Integrated File Watcher, which monitors a specific folder, and notifies through WhatsApp to the authorized person, once changes occur in that target folder


### Purpose of this task
In this current occasion, each and every process becoming automated. No one can wait for a long process until it finishes its job. 
Mainly, in IT industries, an employee or a team, cannot wait for a particular file to be received from a client or any others. To overcome those scenarios, this project will be helpful.

### Design Approach
This project is programmed in Python language. To integrate WhatsApp with the program, Twilio WhatsApp API has been configured with the recipient WhatsApp number. Also, to connect with Sheets, Google API has to be enabled for the respective google account.

### WhatsApp API
To get notification through WhatsApp, a sandbox is to be activated by giving a recipient number. From the recipient number, to activate sandbox, a command, ‘join income-thought’ should be sent to API number.

### Google Sheets API
To access the google sheet using python, there is special package called ‘gspread’ is to be used.  Also, Google API should be enabled and the sheet should be shared to that project API account.
  
### Watchdog observer
Watchdog is a package which observes the targeted folder, and will notifies changes happening in that folder.
