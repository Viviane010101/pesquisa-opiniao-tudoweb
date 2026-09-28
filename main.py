print("======================================")
print("       PESQUISA DE OPINIÃO - TUDOWEB")
print("======================================")

excelente = 0
bom = 0
ruim = 0

for i in range(1, 51):

    print(f"\n--- Entrevistado {i} de 50 ---")

    nome = input("📝 Nome: ")
    idade = int(input("🎂 Idade: "))

    print("\n💬 Como você avalia nosso atendimento?")
    print("⭐ 1 - EXCELENTE")
    print("👍 2 - BOM")
    print("😞 3 - RUIM")

    opiniao = int(input("👉 Digite sua opção: "))

    if opiniao == 1:
        excelente += 1
        print(f"🌟 {nome}, obrigado pela sua excelente avaliação!")

    elif opiniao == 2:
        bom += 1
        print(f"👍 {nome}, obrigado pela sua avaliação!")

    elif opiniao == 3:
        ruim += 1
        print(f"💡 {nome}, obrigado pela sua avaliação!")
        print("Sua opinião nos ajuda a identificar pontos de melhoria.")

    else:
        print("⚠️ Opção inválida.")

total_respostas = excelente + bom + ruim

print("\n======================================")
print("          📊 RESULTADO DA PESQUISA")
print("======================================")

print(f"⭐ EXCELENTE: {excelente}")
print(f"👍 BOM:       {bom}")
print(f"😞 RUIM:      {ruim}")
print("--------------------------------------")
print(f"📋 TOTAL DE RESPOSTAS: {total_respostas}")

print("\n======================================")
print("       💙 AGRADECEMOS SUA OPINIÃO!")
print("======================================")

print("🙏 A TudoWeb agradece sua participação")
print("na nossa pesquisa de satisfação!")

print("\n💬 Sua opinião é muito importante para nós.")
print("💡 Tem alguma sugestão de melhoria?")
print("📩 Entre em contato com nosso canal de atendimento")
print("e compartilhe sua ideia conosco!")

print("\n🚀 Sua sugestão pode contribuir para")
print("melhorarmos cada vez mais nosso atendimento.")
print("\n✨ Obrigado por contribuir com a TudoWeb! ✨")
