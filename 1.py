import tkinter as tk
import webbrowser

# بيانات الصيدليات مع إضافة إحداثيات الخريطة (Latitude, Longitude)
pharmacies_data = {
    "central": {
        "name": "Central Pharmacy",
        "arabic_name": "صيدلية المركز",
        "contract": "متعاقد رسمي",
        "doctors_count": "2",
        "doctor_name": "د. أحمد محمود",
        "qualifications": "ماجستير صيدلة إكلينيكية (جامعة القاهرة)",
        "info": "خدمة 24 ساعة - متوفر أدوية طوارئ وعناية مركزة",
        "lat": 30.0444, "lng": 31.2357  # إحداثيات افتراضية (القاهرة)
    },
    "jabal": {
        "name": "Jabal Pharmacy",
        "arabic_name": "صيدلية الجبل",
        "contract": "غير متعاقد",
        "doctors_count": "1",
        "doctor_name": "د. سارة علي",
        "qualifications": "بكالوريوس صيدلة (جامعة عين شمس)",
        "info": "متوفر الحالات التحويلية والأدوية العامة",
        "lat": 30.0500, "lng": 31.2500
    },
    "ghazali": {
        "name": "Al-Ghazali Pharmacy",
        "arabic_name": "صيدلية الغزالي",
        "contract": "غير متعاقد",
        "doctors_count": "3",
        "doctor_name": "د. محمد حسن",
        "qualifications": "دكتوراه في الصيدلانيات والإكلينيكية",
        "info": "مواعيد صباحية ومسائية - استشارات دوائية",
        "lat": 30.0333, "lng": 31.2333
    },
    "mujtahid": {
        "name": "Al-Mujtahid Pharmacy",
        "arabic_name": "صيدلية المجتهد",
        "contract": "متعاقد رسمي",
        "doctors_count": "2",
        "doctor_name": "د. مريم خالد",
        "qualifications": "بكالوريوس صيدلة إكلينيكية",
        "info": "متوفر أدوية الأمراض المزمنة والتوصيل المنزلي",
        "lat": 30.0600, "lng": 31.2200
    },
}

current_selected_pharmacy = None

# إعداد نافذة التطبيق
root = tk.Tk()
root.title("دليل الصيدليات والأطباء - نظام سطح المكتب")
root.geometry("900x580")
root.configure(bg="#F8F9FA")
root.resizable(False, False)

# رأس التطبيق العلوي
header = tk.Label(
    root,
    text="نظام إدارة وعرض دليل الصيدليات والأطباء والخريطة",
    bg="#1A365D",
    fg="white",
    font=("Arial", 16, "bold"),
    pady=15,
)
header.pack(fill="x")

main_frame = tk.Frame(root, bg="#F8F9FA")
main_frame.pack(fill="both", expand=True, padx=15, pady=15)

# القسم الأيمن (البحث والقائمة)
right_container = tk.Frame(main_frame, bg="#F8F9FA")
right_container.pack(side="right", fill="y", padx=(10, 0))

search_frame = tk.Frame(right_container, bg="#F8F9FA")
search_frame.pack(fill="x", pady=(0, 10))

search_entry = tk.Entry(search_frame, font=("Arial", 12), justify="right", bd=1, relief="solid")
search_entry.pack(side="right", expand=True, fill="x", ipady=6, padx=(5, 0))

def open_map():
    if current_selected_pharmacy:
        lat = current_selected_pharmacy['lat']
        lng = current_selected_pharmacy['lng']
        url = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
        webbrowser.open(url)
    else:
        details_label.config(text="الرجاء اختيار صيدلية أولاً لعرض مكانها على الخريطة.")

def show_details(data):
    global current_selected_pharmacy
    current_selected_pharmacy = data
    
    details_text = (
        f"اسم الصيدلية (بالإنجليزية): {data['name']}\n\n"
        f"اسم الصيدلية (بالعربية): {data['arabic_name']}\n\n"
        f"حالة التعاقد: {data['contract']}\n\n"
        f"عدد الأطباء المتواجدين: {data['doctors_count']}\n\n"
        f"اسم الطبيب المسؤول: {data['doctor_name']}\n\n"
        f"المؤهلات والشهادات: {data['qualifications']}\n\n"
        f"معلومات إضافية: {data['info']}"
    )
    details_label.config(text=details_text)
    map_btn.config(state="normal") # تفعيل زر الخريطة عند اختيار صيدلية

def search_pharmacy():
    query = search_entry.get().strip().lower()
    if not query:
        details_label.config(text="الرجاء إدخال اسم الصيدلية للبحث أولاً.")
        return
    for data in pharmacies_data.values():
        if query in data["name"].lower() or query in data["arabic_name"].lower():
            show_details(data)
            return
    details_label.config(text="عذراً، لم يتم العثور على الصيدلية المطلوبة.")

search_btn = tk.Button(
    search_frame,
    text="بحث",
    bg="#1A365D",
    fg="white",
    font=("Arial", 11, "bold"),
    command=search_pharmacy,
    padx=15,
    bd=0,
    cursor="hand2"
)
search_btn.pack(side="left", ipady=4)

# إطار قائمة الصيدليات
list_frame = tk.LabelFrame(
    right_container,
    text=" قائمة الصيدليات ",
    bg="white",
    fg="#1A365D",
    font=("Arial", 12, "bold"),
    labelanchor="ne",
    padx=10,
    pady=10
)
list_frame.pack(fill="both", expand=True)

for data in pharmacies_data.values():
    btn = tk.Button(
        list_frame,
        text=f"{data['arabic_name']} ({data['contract']})",
        bg="#EDF2F7",
        fg="#1A365D",
        font=("Arial", 11),
        anchor="center",
        pady=8,
        bd=0,
        cursor="hand2",
        command=lambda d=data: show_details(d)
    )
    btn.pack(fill="x", pady=5)

# القسم الأيسر (تفاصيل الصيدلية ومعها زر الخريطة)
left_container = tk.Frame(main_frame, bg="#F8F9FA")
left_container.pack(side="left", fill="both", expand=True)

details_frame = tk.LabelFrame(
    left_container,
    text=" تفاصيل الطبيب والصيدلية وموقع الخريطة ",
    bg="white",
    fg="#1A365D",
    font=("Arial", 12, "bold"),
    labelanchor="ne",
    padx=15,
    pady=15
)
details_frame.pack(fill="both", expand=True)

details_label = tk.Label(
    details_frame,
    text="اختر صيدلية من القائمة الجانبية أو ابحث عنها لعرض التفاصيل وموقعها...",
    bg="white",
    fg="#2D3748",
    font=("Arial", 11),
    justify="right",
    anchor="ne",
    wraplength=420
)
details_label.pack(fill="both", expand=True, pady=(0, 10))

# زر عرض الخريطة الحقيقية
map_btn = tk.Button(
    details_frame,
    text="🌍 عرض موقع الصيدلية على خرائط جوجل (Map)",
    bg="#2B6CB0",
    fg="white",
    font=("Arial", 11, "bold"),
    command=open_map,
    state="disabled", # معطل حتى يتم اختيار صيدلية
    pady=8,
    bd=0,
    cursor="hand2"
)
map_btn.pack(fill="x", pady=5)

root.mainloop()