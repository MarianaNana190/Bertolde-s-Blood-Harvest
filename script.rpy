# script.rpy — Bertolde's Blood Harvest
# Coloque este arquivo dentro da pasta game/ do projeto Ren'Py.


# ============================================================
# PERSONAGENS
# ============================================================

define n = Character("Narrador", color="#C49A3A")
define k = Character("Kaleb", color="#E6C76A")
define p = Character("Pietra", color="#E6C76A")
define d = Character("Diego", color="#E6C76A")
define b = Character("Bill", color="#E6C76A")
define you = Character("[player_name]", color="#F3E7C8")


# ============================================================
# VARIÁVEIS
# ============================================================

default player_name = "You"


# ============================================================
# IMAGENS
# ============================================================

image bg estrada_terra = "images/bg_estrada_terra.jpg"
image bg plantacao_milho = "images/bg_plantacao_milho.jpg"

image bg corvo_observando:
    "images/Fundo.corvo.png"
    xsize 1920
    ysize 1080

image bg mao_bertolde :
    "images/bg_mao_bertolde.jpg"
    xsize 1920
    ysize 1080
                 
image bg bertolde_apertando :
    "images/bg_bertolde_apertando.jpg"
    xsize 1920
    ysize 1080
image bg protagonista_fugindo:
    "images/bg_protagonista_fugindo.jpg"
    xsize 1920
    ysize 1080
image bg casa_fazenda:
    "images/bg_casa_fazenda.jpg"
    xsize 1920
    ysize 1080

image bg fazendeiro_matando:
    "images/bg_fazendeiro_matando.jpg"
    xsize 1920
    ysize 1080
        
image bg bad_end = "images/bg_bad_end.png"
image bg final_bom:
    "images/Final-Milhastico.jpeg"
    xsize 1920
    ysize 1080
image bg final_ruim_fazendeiro:
    "images/bg_final_ruim_fazendeiro.png"
    xsize 1920
    ysize 1080

image nota_desenvolvedor:
    "nota-do-desenvolvedor.png"
    xsize 1920
    ysize 1080
image logo_renpy = "images/logo-renpy.png"

image kaleb = "images/Kaleb.Normal.png"
image pietra = "images/Pietra.Normal.png"
image diego = "images/Diego.Normal.png"
image bertolde = "images/bertolde.png"
image bill = "images/Bill.normal.png"


# ============================================================
# POSIÇÃO DOS PERSONAGENS
# ============================================================

transform personagem_centro:
    xalign 0.5
    yalign 1.0
    yanchor 1.0
    zoom 2.20


# ============================================================
# TRANSIÇÕES
# ============================================================

define dissolve_fast = Dissolve(0.25)
define fade_scene = Fade(0.5, 0.2, 0.5)


# ============================================================
# INÍCIO DO JOGO
# ============================================================

label start:
    jump nota_desenvolvedor


# ============================================================
# NOTA DO DESENVOLVEDOR
# ============================================================

label nota_desenvolvedor:

    scene black with fade_scene

    show nota_desenvolvedor:
        xalign 0.5
        yalign 0.5

    with dissolve_fast

    pause

    hide nota_desenvolvedor with dissolve_fast

    jump configuracao_protagonista


# ============================================================
# CONFIGURAÇÃO DO PROTAGONISTA
# ============================================================

label configuracao_protagonista:

    n "Antes de começarmos..."
    n "Como você gostaria de ser chamado?"

    $ player_name = renpy.input("Qual é o seu nome?", length=20).strip()

    if player_name == "":
        $ player_name = "You"

    n "Certo, [player_name]. A história vai começar."

    jump cena_1


# ============================================================
# CENA 1
# ============================================================

label cena_1:

    scene bg estrada_terra with fade_scene

    n "A estrada de terra parecia não ter fim. O carro sacudia tanto que quase fazia os dentes irem ao chão. No banco do passageiro, a ideia absurda dos seus amigos de repente virou parar o veículo perto do acostamento."

    show diego at personagem_centro with dissolve_fast

    d "Vamos lá, gente! É só entrar, pegar uns milhos e voltar. Ninguém vai nem ver!"

    you "Eu acho uma péssima ideia... Está breu total lá fora e a gente nem conhece essa fazenda."

    hide diego with dissolve_fast

    show pietra at personagem_centro with dissolve_fast

    p "Deixa de ser medroso!"

    hide pietra with dissolve_fast

    scene bg plantacao_milho with fade_scene

    n "Vocês quatro pulam para fora, rindo baixo, e entram direto na plantação escura para pegar os milhos."

    show diego at personagem_centro with dissolve_fast

    d "Cara, pega o máximo que conseguir!"

    you "Tem certeza? Esse lugar me dá um arrepio..."


    # ========================================================
    # CUTSCENE DO CORVO
    # ========================================================
    # Primeiro o narrador fala.
    # Quando o jogador avançar o diálogo,
    # o vídeo começa imediatamente.
    # ========================================================

    n "De repente, um corvo solta um grasnado alto no alto, assustando vocês."

    $ renpy.movie_cutscene("videos/cutscene_corvo.mp4")


    # ========================================================
    # DEPOIS DA CUTSCENE
    # ========================================================

    scene bg corvo_observando with fade_scene

    n "Então o corvo grunhiu, e vocês escutaram um som de palha se retorcendo ecoando ao lado de vocês."

    n "Vocês decidem seguir de onde estava vindo o som de palha."

    show kaleb at personagem_centro with dissolve_fast

    k "Que som foi esse?"

    hide kaleb with dissolve_fast

    scene bg plantacao_milho with fade_scene

    show bertolde at personagem_centro with dissolve_fast

    n "Iluminado pela lua, Bertolde surge entre as fileiras de milho. Seus olhos de costura parecem encarar cada um de vocês."

    hide bertolde with dissolve_fast

    scene black with fade_scene

    n "Em pânico absoluto, seus amigos saem correndo desordenados de volta para o carro, entram, pisam no acelerador e abandonam você para trás no escuro."

    n "Você está sozinho com aquele monstro."

    menu:

        "TENTAR ALCANÇAR CARRO":
            jump caminho_carro

        "CORRER ATÉ UMA CASA":
            jump caminho_casa


# ============================================================
# CAMINHO DO CARRO
# ============================================================

label caminho_carro:

    scene black with fade_scene

    n "Você tentou correr o mais rápido possível, porém seus amigos já tinham ido embora."

    n "Sua outra opção foi tentar se esconder dentro de uma vala."

    n "Porém o corvo, pet de Bertolde, raspa as garras em seu rosto."

    n "Antes que você possa se levantar, mãos rígidas compostas de madeira e palha prendem seus pulsos com força sobre-humana."

    scene bg mao_bertolde with fade_scene

    you "Me solta! Me solta!"

    menu:

        "MORDER":
            jump caminho_morder

        "DEBATER-SE":
            jump caminho_debater


# ============================================================
# MORDE — FINAL RUIM 1
# ============================================================

label caminho_morder:

    scene bg mao_bertolde with dissolve_fast

    you "Tentei morder o espantalho, mas logo me arrependi quando senti uma dor indescritível no meu dente."

    you "O corpo dele era feito de cano PVC, não de palha, e com a mordida meus dentes quebraram."

    with hpunch

    you "Quando ele me soltou no chão, eu bati a cabeça na vala. Senti o gosto de sangue vindo da minha boca."

    you "Cuspi o sangue e, junto do sangue, saíram dois dentes. Quando tentei tomar forças para fugir, ouvi o som de um corvo."

    you "Quando abri os olhos, vi um corvo atacando meu rosto e, em seguida, ouvi passos pesados."

    scene bg bertolde_apertando with fade_scene

    n "Era Bertolde. O espantalho pegou seu pescoço e o apertou com todas as forças."

    with hpunch

    n "Você perdeu a consciência."

    jump final_ruim_morder


# ============================================================
# FINAL RUIM — MORDE
# ============================================================

label final_ruim_morder:

    scene bg bad_end with fade_scene

    pause

    jump creditos


# ============================================================
# DEBATER-SE — FINAL BOM
# ============================================================

label caminho_debater:

    scene bg mao_bertolde with dissolve_fast

    you "Comecei a me debater da forma mais exagerada que conseguia."

    you "Foi então que consegui chutar o espantalho."

    you "Ele caiu no chão, revelando seu abdômen, onde havia uma placa protoboard, um Arduino e vários cabos."

    you "Quem será que te criou?"

    you "Aproveitei que ele estava inconsciente e dei mais um chute nele. Porém, quando fui chutá-lo mais uma vez, o corvo começou a me atacar."

    n "Você jogou um milho no pássaro, que caiu com o impacto."

    scene bg protagonista_fugindo with fade_scene

    n "Você pegou os milhos que tinha colhido e saiu correndo pela estrada."

    n "Depois de 20 minutos andando, você conseguiu carona com um desconhecido."

    jump final_bom


# ============================================================
# FINAL BOM
# ============================================================

label final_bom:

    scene bg final_bom with fade_scene

    pause

    jump creditos


# ============================================================
# CAMINHO DA CASA — FINAL RUIM 2
# ============================================================

label caminho_casa:

    scene black with fade_scene

    you "Vi uma casa no meio da plantação, tinha uma luz acesa. Com os milhos em minhas mãos, corri o mais rápido que pude."

    scene bg casa_fazenda with fade_scene

    you "Quando cheguei até o casarão, comecei a bater na porta desesperadamente."

    you "Socorro! Tem um espantalho vivo na sua plantação!"

    n "A porta se abre. O Fazendeiro surge na penumbra segurando um garfo de feno nas mãos, com o rosto dominado pela raiva ao ver o milho na sua mão."

    show bill at personagem_centro with dissolve_fast

    b "Mais um invasor roubando minha colheita? Na minha terra, ladrão não sai andando."

    b "Se meu 'fih' não deu conta de eliminar uma praga, eu mesmo elimino."

    n "O fazendeiro ergue o garfo de feno."

    scene black with fade_scene

    n "Então você sente um impacto muito forte em seu abdômen."

    with hpunch

    n "Não demora muito e você vê o sangue jorrando no chão. Você acaba perdendo a consciência."

    scene bg fazendeiro_matando with fade_scene

    jump final_ruim_fazendeiro


# ============================================================
# FINAL RUIM — FAZENDEIRO
# ============================================================

label final_ruim_fazendeiro:

    scene bg final_ruim_fazendeiro with fade_scene

    pause

    jump creditos


# ============================================================
# CRÉDITOS
# ============================================================

transform tamanho_logo_renpy:

    xalign 0.5
    zoom 0.45


transform rolagem_creditos:

    xalign 0.5
    yalign 1.15

    linear 8.0 yalign -1.20


screen tela_creditos():

    vbox:

        at rolagem_creditos

        xalign 0.5
        spacing 12

        text "CRÉDITOS:":

            xalign 0.5
            text_align 0.5
            color "#C49A3A"
            size 38

        text "PROGRAMAÇÃO: Mariana\n\nILUSTRAÇÃO: Maria Vitória\n\nROTEIRO: Mariana\n\nProfessores: Simon & Roberty\n\ndesenvolvido com":

            xalign 0.5
            text_align 0.5
            color "#F3E7C8"
            size 25

        add "logo_renpy" at tamanho_logo_renpy


# ============================================================
# LABEL DOS CRÉDITOS
# ============================================================

label creditos:

    scene black with fade_scene

    show screen tela_creditos

    pause 8.0

    hide screen tela_creditos

    return
