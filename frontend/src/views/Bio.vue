<template>
  <div class="flex w-full flex-col items-center px-6 py-5">
    <div class="!w-[992px] max-w-full space-y-4">
      <div class="flex items-end">
        <div class="h-28 w-28 min-w-28 rounded-lg bg-gray-300" />
        <h1 class="ml-4 w-fit text-4xl font-semibold text-[#0047FF]">
          Michael Karpow
        </h1>
      </div>
      <div class="flex flex-wrap gap-x-8 gap-y-6">
        <div class="item !w-[360px]">
          <h6 class="item-header">Education</h6>
          <div class="mt-3 flex items-center justify-center">
            <img class="h-24 w-24 rounded" src="@/assets/tuni.png" alt="tuni" />
            <div class="ml-4 flex flex-col font-semibold">
              <p class="leading-4 text-gray-400">2022-2026</p>
              <p class="leading-5">
                Tampere University<br />of Applied Sciences
              </p>
              <p class="leading-4 text-gray-400">Software Engineering</p>
            </div>
          </div>
        </div>
        <div class="item !w-[500px]">
          <h6 class="item-header">IT skills</h6>
          <p>
            <b>Languages:</b> HTML, JavaScript, CSS, Python, SQL
            <br />
            <b>Frameworks:</b> Vue.js, React.js, Express.js, TailwindCSS,
            FastAPI, SQLAlchemy, pytest, Jest, Cypress
            <br />
            <b>Operating systems:</b> Linux, Windows
            <br />
            <b>Other tools:</b> Selenium, Docker, Nginx, GitHub CI/CD, git
          </p>
        </div>
      </div>
      <div class="flex flex-wrap gap-x-8 gap-y-6">
        <div class="item !w-[600px]">
          <h6 class="item-header">About</h6>
          <p>
            &emsp;I have a passion for learning modern technologies and applying
            them to my work.
            <br />
            &emsp;Moreover, I like participating in cybersecurity competitions
            (CTFs) in my free time. This helps me to look at my code from the
            perspective of a potential attacker during programming.
            <br />
            &emsp;Also, I participate in programming contests which help me to
            write optimized code.
          </p>
        </div>

        <div class="item flex w-full flex-col items-center">
          <h6 class="item-header">Contact Info</h6>
          <div class="mt-2">
            <a href="tel:0442422577" class="hover:underline"
              >+358 44 242 2577
            </a>
            <br />
            <a href="mailto:michael.karpow@hotmail.com" class="hover:underline">
              michael.karpow@hotmail.com
            </a>
            <br />
            <a href="https://github.com/M1h4n1k" class="hover:underline">
              github.com/M1h4n1k</a
            >
            <br />
            <a href="https://linkedin.com/in/mkarpow" class="hover:underline">
              linkedin.com/in/mkarpow
            </a>
          </div>
        </div>
      </div>
      <h1 class="!mt-6 text-3xl font-semibold text-[#0047FF]">
        Working experience
      </h1>
      <div class="!mt-3 flex flex-wrap gap-x-8 gap-y-6">
        <div class="item relative !w-[400px] min-w-[480px] space-y-2">
          <div>
            <h6 class="text-lg font-bold leading-5">Software developer</h6>
            <h5 class="text-sm font-semibold">Jun 2023 - Dec 2023</h5>
          </div>
          <p>
            Full-stack developer on MeteorJS with ReactJS at Unfair Advantage
            (<a class="hover:underline" href="https://stafftribes.com/about"
              >stafftribes.com</a
            >) — a social network for sportsmen with lots of legacy code
          </p>
          <p>
            <span class="font-semibold">Communication language:</span> English
          </p>
          <div>
            <span class="font-semibold">Achievements/tasks:</span>
            <ul class="list-inside list-disc">
              <li>Reported several security issues of high importance</li>
              <li>Reviewed other people’s code</li>
              <li>Worked closely with product manager</li>
            </ul>
          </div>
          <div class="h-6"></div>
          <p class="absolute bottom-4 right-4 text-sm italic">
            Reference:
            <a class="hover:underline" href="mailto:paul@tribenetworks.ai"
              >paul@tribenetworks.ai</a
            >
          </p>
        </div>
        <div class="item relative !w-[400px] min-w-[480px] space-y-2">
          <div>
            <h6 class="text-lg font-bold leading-5">Owner/programmer</h6>
            <h5 class="text-sm font-semibold">Apr 2020 - now</h5>
          </div>
          <p>
            Developed several projects from scratch some of which are quite
            popular (~1k daily users according to google analytics)
          </p>
          <p>
            <span class="font-semibold">Keywords:</span> integrating API,
            parsing, REST API, git, SQL and NoSQL databases, fastAPI, VueJS,
            ReactJS, Python3, JavaScript, learning TypeScript, administrating
            Linux servers, Docker
          </p>
          <div class="h-6"></div>
          <p class="absolute bottom-4 right-4 text-sm italic">
            Reference:
            <a class="hover:underline" href="https://github.com/M1h4n1k"
              >https://github.com/M1h4n1k</a
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.item {
  width: fit-content;
  border-radius: 1.5rem;
  background-color: rgb(243 244 246);
  padding: 1rem 1.5rem;
  min-width: 250px;
  flex-grow: 1;
}

.item-header {
  width: 100%;
  font-weight: 600;
  font-size: 1.125rem;
  line-height: 1.75rem;
  text-align: center;
}
</style>
