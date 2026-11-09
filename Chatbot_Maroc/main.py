import base64
import streamlit as st

# 1. Configuration de la page
st.set_page_config(
    page_title="Quiz - Unité Territoriale du Maroc",
    page_icon="🇲🇦",
    layout="centered",
)


# Fonction pour encoder l'image locale en base64 (الخلفية)
def get_base64_image(image_path):
  try:
    with open(image_path, "rb") as img_file:
      return base64.b64encode(img_file.read()).decode()
  except FileNotFoundError:
    return None


img_base64 = get_base64_image("background.png")

if img_base64:
  bg_style = f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(15, 12, 41, 0.75), rgba(48, 43, 99, 0.75)), 
                    url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        background-color: #0f0c29;
    }}
    </style>
    """
else:
  bg_style = """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    </style>
    """

st.markdown(bg_style, unsafe_allow_html=True)

# 2. Style CSS général
st.markdown(
    """
    <style>
    h3 {
        color: #FFFFFF !important;
        font-weight: 700;
        font-size: 1.3rem !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
    }
    .stRadio label p {
        color: #FFFFFF !important;
        font-size: 1.15rem !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
    }
    div[data-testid="stExpander"] * {
        color: #FFFFFF !important;
        font-size: 1.1rem !important;
    }
    .stButton>button {
        background-color: #006233;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 12px 24px;
        border: none;
        width: 100%;
        font-size: 1.15rem;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #004d28;
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. الشريط الجانبي بمعلوماتكِ والمعرض الوثائقي (مضاف إليه مجلس الأمن)
with st.sidebar:
  st.image(
      "https://upload.wikimedia.org/wikipedia/commons/2/2c/Flag_of_Morocco.svg",
      width=100,
  )
  st.title("🇲🇦 À propos du Quiz")
  st.info("""
    **📚 Thème :** Histoire, Diplomatie & Autonomie
    **❓ Questions :** 10 Questions Stratégiques
    """)

  st.write("---")

  st.success("""
    **👩‍🎓 Fait par :** Aya Hajoui
    **🏫 Établissement :** Lycée Arrachad
    **📌 Option :** International
    """)

  st.write("---")
  st.subheader("🖼️ معرض وثائقي وتاريخي")

  st.image(
      "https://i1.hespress.com/wp-content/uploads/2020/11/marche_verte_259245790.jpg",
      caption="المسيرة الخضراء المظفرة (1975)",
      use_container_width=True,
  )

  st.image(
      "https://upload.wikimedia.org/wikipedia/commons/2/2d/2024-11-18-Headquarters_of_the_United_Nations-0605.jpg",
      caption="مجلس الأمن الدولي - القرارات الأممية",
      use_container_width=True,
  )

  st.image(
      "https://i1.hespress.com/wp-content/uploads/2023/01/Bahija-Simo-manuscript-Historique-royale4.jpg",
      caption="وثائق تاريخية وظهائر ملكية",
      use_container_width=True,
  )

  st.image(
      "https://www.sahara24.net/static/uploads/2024/01/098.jpg",
      caption="التنمية الحضرية الحديثة (العيون)",
      use_container_width=True,
  )

  st.write("---")
  if st.button("🔄 Réinitialiser le Quiz"):
    for key in list(st.session_state.keys()):
      del st.session_state[key]
    st.rerun()

# 4. En-tête principal avec le titre et le slogan
st.markdown(
    """
    <div style="background: linear-gradient(135deg, rgba(141, 20, 36, 0.95), rgba(26, 83, 49, 0.95)); padding: 30px; border-radius: 15px; text-align: center; color: white; box-shadow: 0 0 25px rgba(0, 166, 81, 0.4), 0 0 25px rgba(193, 39, 45, 0.4); margin-bottom: 25px; border: 1px solid rgba(255, 255, 255, 0.2);">
        <h1 style="font-size: 2.2rem; font-weight: 800; margin-bottom: 10px; color: #ffffff; text-shadow: 0 0 10px rgba(255,255,255,0.6), 0 0 20px rgba(0,166,81,0.4);">🇲🇦 الوحدة الترابية للمغرب : تاريخ، سيادة وتنمية</h1>
        <p style="font-size: 1.2rem; color: #FFD700; font-weight: 600; margin-top: 5px; text-shadow: 0 0 8px rgba(0,0,0,0.6);">"عيد الوحدة ينادينا، ومستقبل نبنيه معاً"</p>
        <p style="font-size: 1.1rem; color: #f0f0f0; margin-top: 10px;">Espace interactif de présentation - Lycée Arrachad</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# 5. صندوق المحطات التاريخية
st.markdown(
    """
    <div style="background: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 10px; border-left: 5px solid #006233; margin-bottom: 25px; color: white;">
        <h4 style="margin: 0 0 8px 0; color: #FFD700;">📌 محطات بارزة في مسار الوحدة الترابية :</h4>
        <p style="margin: 0; font-size: 1.05rem; line-height: 1.6;">
        • استرجاع سيدي إفني (1969) &nbsp;|&nbsp; 
        • المسيرة الخضراء المظفرة (1975) &nbsp;|&nbsp; 
        • استرجاع إقليم وادي الذهب (1979)
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# 6. Formulaire du Quiz (10 أسئلة)
with st.form("quiz_form"):
  st.markdown("##### 📊 التقدم في الاختبار / Progression du Quiz")
  st.progress(100)
  st.write("---")

  # --- Question 1 ---
  st.subheader("Question 1 : La Marche Verte")
  q1 = st.radio(
      "Quel événement historique majeur a marqué la récupération des provinces"
      " du Sud en 1975 ?",
      [
          "Sélectionnez une option...",
          "Le Manifeste de l'Indépendance",
          "L'organisation de la Marche Verte",
          "L'accord d'Algeciras",
      ],
      key="q1",
  )
  st.write("")

  # --- Question 2 ---
  st.subheader("Question 2 : Définition de l'Autonomie (مفهوم الحكم الذاتي)")
  q2 = st.radio(
      "Que signifie fondamentalement l'initiative d'autonomie pour les"
      " provinces du Sud sous souveraineté marocaine ?",
      [
          "Sélectionnez une option...",
          (
              "Une gestion par les habitants de leurs affaires locales dans le"
              " cadre de la souveraineté du Royaume"
          ),
          "Une séparation totale de l'État central",
          "Une administration directe internationale",
      ],
      key="q2",
  )
  st.write("")

  # --- Question 3 ---
  st.subheader("Question 3 : Autonomie vs Indépendance")
  q3 = st.radio(
      "Quelle est la différence fondamentale entre le plan d'autonomie et"
      " l'indépendance totale ?",
      [
          "Sélectionnez une option...",
          (
              "L'autonomie s'exerce sous la souveraineté nationale et l'unité"
              " du drapeau, contrairement à la sécession"
          ),
          "Il n'y a aucune différence sur le plan juridique",
          "L'autonomie annule complètement les lois nationales",
      ],
      key="q3",
  )
  st.write("")

  # --- Question 4 ---
  st.subheader("Question 4 : Date du مقترح الحكم الذاتي")
  q4 = st.radio(
      "En quelle année le Royaume du Maroc a-t-il soumis son initiative"
      " d'autonomie au Conseil de sécurité de l'ONU ?",
      ["Sélectionnez une option...", "2007", "1999", "2011"],
      key="q4",
  )
  st.write("")

  # --- Question 5 ---
  st.subheader("Question 5 : Compétences de l'État Central (اختصاصات الدولة)")
  q5 = st.radio(
      "Parmi les domaines suivants, lequel reste strictly de la compétence"
      " exclusive de l'État central dans le plan d'autonomie ?",
      [
          "Sélectionnez une option...",
          "La défense nationale, la monnaie et les attributs de la souveraineté",
          "L'urbanisme local et l'artisanat",
          "La gestion des foires régionales",
      ],
      key="q5",
  )
  st.write("")

  # --- Question 6 ---
  st.subheader(
      "Question 6 : Rôle de l'ONU (دور الأمم المتحدة والدعم الدولي)"
  )
  q6 = st.radio(
      "Comment le Conseil de sécurité de l'ONU qualifie-t-il régulièrement"
      " l'initiative marocaine d'autonomie ?",
      [
          "Sélectionnez une option...",
          "Sérieuse, crédible et base de compromis pour une solution",
          "Une option temporaire sans lendemain",
          "Une proposition nécessitant un amendement total",
      ],
      key="q6",
  )
  st.write("")

  # --- Question 7 ---
  st.subheader("Question 7 : Développement et Investissement (التنمية)")
  q7 = st.radio(
      "Quel impact le Nouveau Modèle de Développement des Provinces du Sud"
      " a-t-il sur la région ?",
      [
          "Sélectionnez une option...",
          (
              "Il dote la région d'infrastructures modernes et stimule la"
              " croissance économique"
          ),
          "Il se limite à des réformes administratives mineures",
          "Il n'a aucun lien avec la population locale",
      ],
      key="q7",
  )
  st.write("")

  # --- Question 8 ---
  st.subheader("Question 8 : Participation Locale (تدبير الشؤون المحلية)")
  q8 = st.radio(
      "Comment le plan d'autonomie garantit-il la participation des"
      " populations locales ?",
      [
          "Sélectionnez une option...",
          (
              "À travers des institutions législatives, exécutives et des"
              " tribunaux locaux élus par les habitants"
          ),
          "En confiant la gestion à des fonctionnaires nommés de l'extérieur",
          "En suspendant toute élection locale",
      ],
      key="q8",
  )
  st.write("")

  # --- Question 9 ---
  st.subheader("Question 9 : Fondement Historique (الرابطة التاريخية)")
  q9 = st.radio(
      "Quel lien spirituel et historique unit les populations du Sud au Trône"
      " Alaouite ?",
      [
          "Sélectionnez une option...",
          "La Baïa (allégeance) historique et perpétuelle",
          "Un simple pacte économique récent",
          "Une convention administrative temporaire",
      ],
      key="q9",
  )
  st.write("")

  # --- Question 10 ---
  st.subheader(
      "Question 10 : Analyse et Diplomatie (الدبلوماسية والحل السياسي)"
  )
  q10 = st.radio(
      "Quelle est l'importance majeure de l'ouverture de consulats généraux"
      " à Laâyoune et Dakhla ?",
      [
          "Sélectionnez une option...",
          (
              "La consécration diplomatique internationale de la marocanité du"
              " Sahara"
          ),
          "Un simple accord touristique saisonnier",
          "Une mesure administrative sans portée politique",
      ],
      key="q10",
  )

  st.write("---")
  submitted = st.form_submit_button("Valider mes réponses et afficher le bilan")

# 7. نتائج الاختبار والأركان المضافة
if submitted:
  score = 0
  total = 10

  if q1 == "L'organisation de la Marche Verte":
    score += 1
  if (
      q2
      == "Une gestion par les habitants de leurs affaires locales dans le cadre"
      " de la souveraineté du Royaume"
  ):
    score += 1
  if (
      q3
      == "L'autonomie s'exerce sous la souveraineté nationale et l'unité du"
      " drapeau, contrairement à la sécession"
  ):
    score += 1
  if q4 == "2007":
    score += 1
  if (
      q5
      == "La défense nationale, la monnaie et les attributs de la"
      " souveraineté"
  ):
    score += 1
  if (
      q6 == "Sérieuse, crédible et base de compromis pour une solution"
  ):
    score += 1
  if (
      q7
      == "Il dote la région d'infrastructures modernes et stimule la"
      " croissance économique"
  ):
    score += 1
  if (
      q8
      == "À travers des institutions législatives, exécutives et des"
      " tribunaux locaux élus par les habitants"
  ):
    score += 1
  if q9 == "La Baïa (allégeance) historique et perpétuelle":
    score += 1
  if (
      q10
      == "La consécration diplomatique internationale de la marocanité du Sahara"
  ):
    score += 1

  st.write("---")
  st.header("📈 Bilan de l'évaluation")
  st.progress(score / total)

  if score == 10:
    st.balloons()
    st.success(
        f"🏆 **Performance Exceptionnelle ({score}/{total}) :** Maîtrise"
        " parfaite et analytique des aspects historiques, politiques et"
        " diplomatiques de l'Unité Territoriale."
    )
  elif score >= 6:
    st.info(
        f"👏 **Bon Niveau ({score}/{total}) :** Solide compréhension des"
        " concepts clés de l'autonomie et de la diplomatie marocaine."
    )
  else:
    st.warning(
        f"📖 **Résultat ({score}/{total}) :** Nous vous invitons à revoir les"
        " axes de l'initiative d'autonomie et de son cadre historique."
    )

  # --- ركن الدبلوماسية الملكية والانفتاح الأطلسي ---
  st.markdown(
      """
        <div style="background: rgba(0, 98, 51, 0.3); padding: 20px; border-radius: 12px; margin-top: 20px; color: white; border: 1px solid #006233;">
            <h3 style="margin-top: 0; color: #FFD700;">🌐 ركن الدبلوماسية الملكية والامتداد الأطلسي :</h3>
            <p style="font-size: 1.05rem; line-height: 1.6; margin-bottom: 10px;">
            تتويجاً للمسار الدبلوماسي الحكيم، تشهد الأقاليم الجنوبية للمملكة تحولاً استراتيجياً كبيراً بفضل المبادرات الملكية السامية، وخاصة <b>المبادرة الأطلسية الرامية إلى تسهيل دخول دول الساحل إلى المحيط الأطلسي</b>، وافتتاح العديد من القنصليات الدولية في العيون والداخلة، مما يؤكد المكانة الإقليمية والدولية البارزة للمغرب.
            </p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  # --- صندوق المحطات الدبلوماسية الدولية ---
  with st.expander(
      "🌍 صندوق المحطات الدبلوماسية الدولية (Le carnet des reconnaissances)"
  ):
    st.markdown("""
        * **دعم القوى الكبرى :** تأكيد مواقف عدد من الشركاء الدوليين (مثل الولايات المتحدة الأمريكية وإسبانيا وفرنسا وعدد من الدول العربية والإفريقية) التي تعتبر مبادرة الحكم الذاتي الأساس الأكثر جدية وواقعية لتسوية هذا النزاع المفتعل.
        * **الدبلوماسية القنصلية :** فتح أكثر من 30 قنصلية عامة لدول شقيقة وصديقة في مدينتي العيون والداخلة، مما يعكس اعترافاً دبلوماسياً عملياً وفعلياً.
        * **حضور قاري ودولي :** ترسيخ الشراكات الاقتصادية والأمنية التي تجعل من الصحراء المغربية بوابة محورية للتواصل بين إفريقيا وأوروبا والأطلسي.
        """)

  # --- خلاصة العرض الختامية ---
  st.markdown(
      """
        <div style="background: linear-gradient(135deg, rgba(0, 98, 51, 0.85), rgba(141, 20, 36, 0.85)); padding: 20px; border-radius: 12px; margin-top: 20px; color: white; border: 1px solid rgba(255,255,255,0.3);">
            <h3 style="margin-top: 0; color: #FFD700;">🌟 خلاصة العرض (Message de Clôture) :</h3>
            <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 0;">
            إن الوحدة الترابية للمغرب ليست مجرد محطة تاريخية عابرة، بل هي مسار مستمر من البناء، التنمية الشاملة، والتلاحم الدائم بين العرش والشعب للدفاع عن ثوابت الوطن ومستقبله الواعد تحت القيادة الرشيدة لجلالة الملك محمد السادس نصره الله.
            </p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  with st.expander("🔍 Afficher le corrigé détaillé et les notes historiques"):
    st.markdown("""
        * **Question 1 :** L'organisation de la **Marche Verte** en 1975 reste l'acte fondateur de la récupération pacifique des provinces du Sud.
        * **Question 2 :** L'**Autonomie** permet aux populations locales de gérer leurs affaires démocratiquement tout en respectant la souveraineté nationale.
        * **Question 3 :** Contrairement à l'indépendance totale, le plan d'autonomie s'inscrit **sous la souveraineté du Royaume**.
        * **Question 4 :** Présenté en **2007**, le projet a marqué un tournant décisif salué par la communauté internationale.
        * **Question 5 :** La **défense et la monnaie** relèvent de la souveraineté exclusive de l'État central.
        * **Question 6 :** L'ONU qualifie l'initiative marocaine de **sérieuse et crédible**.
        * **Question 7 :** Le **Nouveau Modèle de Développement** transforme radicalement les infrastructures des provinces du Sud.
        * **Question 8 :** La participation locale se fait par le biais d'**institutions élues** (législatives et exécutives).
        * **Question 9 :** La **Baïa** demeure le ciment spirituel et historique unissant les provinces du Sud au Trône.
        * **Question 10 :** L'ouverture des **consulats à Laâyoune et Dakhla** consacre la reconnaissance internationale de la marocanité du Sahara.
        """)