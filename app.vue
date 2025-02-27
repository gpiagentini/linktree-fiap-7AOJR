<script setup lang="ts">
import GoToButton from './components/GoToButton.vue';

const aboutMeText = `
Engenheiro de Software com 5 anos de experiência, especializado em desenvolvimento back-end utilizando Java (JSF e Spring) e Python para automação e web-scraping. Possuo também experiência com Node.js, especialmente na construção de arquiteturas BFF (Backend-for-Frontend) e integração de microsserviços. No front-end, tenho conhecimentos sólidos em frameworks como React, Vue.js e Angular, além de habilidades com HTML e CSS.
Possuo ampla experiência em colaboração com equipes multidisciplinares, atuando em ambientes ágeis com metodologias como Scrum, além de participar ativamente da resolução de problemas críticos em sistemas financeiros, garantindo operações eficientes e implementações robustas.
Por ter trabalhado em sistemas críticos voltados ao mercado financeiro, tenho experiência em resolução de problemas sob pressão e trabalho em equipe, além de desenvolver boa comunicação para entender requisitos e abstraí-los para funcionalidades nos sistemas.
`;
</script>

<template>
  <ProfileInfo title="Gabriel Martins Teixeira Piagentini" quote="Desenvolvedor FullStack" profile="photo.jpg" />
  <div class="flex flex-col w-4/5 mx-auto space-y-8">
    <Section title="Sobre mim" :text="aboutMeText" />
    <div class="w-1/5 mx-auto pt-3 text-center space-y-4">
      <GoToButton dest="Linkedin" url="https://www.linkedin.com/in/gpiagentini/" icon="👔" />
      <GoToButton dest="Github" url="https://github.com/gpiagentini/" icon="💻" />
      <GoToButton dest="WhatsApp" url="https://wa.me/+5511995117433" icon="💬" />
      <GoToButton dest="E-mail" url="mailto:gmtpiagentini@gmail.com" icon="📨" />
      <GoToButton dest="Personal Website" url="https://www.gpiagentini.com" icon="😎" />
    </div>
  </div>
</template>
