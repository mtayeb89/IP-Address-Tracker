# IP-Address-Tracker
Python script is designed to track IP addresses assigned to devices within your local network. 
English Version
IP Address Tracker

Description:
This Python script is designed to track IP addresses assigned to devices within your local network. It scans the entire network, identifies active devices, and logs their IP addresses to a file. This tool is useful for network administrators or IT managers working in environments where IP addresses frequently change (e.g., DHCP-enabled networks).
Features:

    Scans the local network to identify active devices.
    Saves active IP addresses to a text file.
    Cross-platform support (works on both Windows and Linux/macOS).
    Simple to use and configure.

How It Works:

    The script retrieves the current device's hostname and IP address.
    It then pings each device in the same subnet (e.g., 192.168.1.x) to check which devices are online.
    The active devices' IP addresses are saved to a file called ip_addresses.txt.

Requirements:

    Python 3.x
    Operating System: Windows, Linux, or macOS

Installation:

    Install Python 3 if it's not already installed. You can download it from Python's official website.
    Download the script and save it as ip_tracker.py.
    Run the script using the command:

    bash

    python ip_tracker.py

Usage:

    Run the script, and it will:
        Display the hostname and IP address of the current device.
        Scan the local network and identify active devices.
        Save active IP addresses to a file named ip_addresses.txt.

Customization:

You can modify the scan_network() function to scan different IP ranges by changing the base IP address.
Security Considerations:

    Running network scans may require administrator privileges on some systems.
    Use the tool responsibly in networks where you have permission to run such scans.

Example Output:

yaml

Device Hostname: my-computer
Device IP Address: 192.168.1.101
Scanning network 192.168.1.0/24...
Device found at: 192.168.1.1
Device found at: 192.168.1.5
Device found at: 192.168.1.102
Active IP addresses saved to ip_addresses.txt.

Arabic Version
متتبع عناوين IP

الوصف:
هذا البرنامج المكتوب بلغة Python مصمم لتتبع عناوين IP المخصصة للأجهزة داخل شبكتك المحلية. يقوم البرنامج بفحص الشبكة بأكملها، ويحدد الأجهزة النشطة، ويسجل عناوين IP الخاصة بها في ملف. هذا الأداة مفيدة لمسؤولي الشبكات أو مديري تكنولوجيا المعلومات الذين يعملون في بيئات تتغير فيها عناوين IP بشكل متكرر (مثل الشبكات التي تستخدم DHCP).
الميزات:

    فحص الشبكة المحلية لتحديد الأجهزة النشطة.
    حفظ عناوين IP النشطة في ملف نصي.
    دعم للأنظمة المتعددة (يعمل على Windows و Linux و macOS).
    سهل الاستخدام والتكوين.

كيفية عمله:

    يسترد البرنامج اسم المضيف الحالي للجهاز وعنوان IP.
    ثم يقوم بإرسال إشارات ping إلى كل جهاز في نفس الشبكة الفرعية (مثل 192.168.1.x) للتحقق من الأجهزة النشطة.
    يتم حفظ عناوين IP الخاصة بالأجهزة النشطة في ملف يسمى ip_addresses.txt.

المتطلبات:

    Python 3.x
    نظام التشغيل: Windows أو Linux أو macOS

التثبيت:

    قم بتثبيت Python 3 إذا لم يكن مثبتًا بالفعل. يمكنك تنزيله من الموقع الرسمي لـ Python.
    قم بتنزيل البرنامج واحفظه باسم ip_tracker.py.
    قم بتشغيل البرنامج باستخدام الأمر التالي:

    bash

    python ip_tracker.py

الاستخدام:

    عند تشغيل البرنامج، سيقوم بما يلي:
        عرض اسم المضيف وعنوان IP الخاص بالجهاز الحالي.
        فحص الشبكة المحلية وتحديد الأجهزة النشطة.
        حفظ عناوين IP النشطة في ملف يسمى ip_addresses.txt.

التخصيص:

يمكنك تعديل وظيفة scan_network() لفحص نطاقات IP مختلفة عن طريق تغيير عنوان IP الأساسي.
اعتبارات الأمان:

    قد يتطلب تشغيل عمليات فحص الشبكة صلاحيات المسؤول على بعض الأنظمة.
    استخدم الأداة بمسؤولية في الشبكات التي لديك إذن بإجراء عمليات الفحص فيها.

مثال على الإخراج:

perl

اسم المضيف: my-computer
عنوان IP الخاص بالجهاز: 192.168.1.101
جارٍ فحص الشبكة 192.168.1.0/24...
تم العثور على جهاز في: 192.168.1.1
تم العثور على جهاز في: 192.168.1.5
تم العثور على جهاز في: 192.168.1.102
تم حفظ عناوين IP النشطة في ip_addresses.txt.

