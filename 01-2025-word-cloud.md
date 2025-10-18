---
title: 2025 is the year of...
---

# 2025

<div id=cloud-container>
  <img id=cloud alt='Word cloud with terms like "ChatGPT" and "model" featured strongly' src=../2025-word-cloud.svg>
</div>
<style>
  #cloud-container {
    width: 848px;
    height: 475px;
    overflow: hidden;
    margin-inline: auto;
    margin-bottom: 1rem;
  }
  #cloud {
    transform: scale(43) translate(-68.5px, -12.25px);
    transition: transform ease-in 3s;
  }
  #zoom {
    display: block;
    margin-inline: auto;
  }
</style>

<button id=zoom>Zoom image</button>
<script>
const cloud = document.querySelector("#cloud");
document.querySelector("#zoom").addEventListener("click", (e) => {
  cloud.style.transform = "scale(2) translate(-68.5px, -12.25px)";
  setTimeout(() => {
    cloud.style.transition = "transform ease-out 2s";
    cloud.style.transform = "scale(1)";
  }, 2500);
});
</script>

(image source: <a href=https://www.weetechsolution.com/blog/best-word-cloud-generators target=_blank rel=noreferrer>7 Best Word Cloud Generators in 2025 (Free and Paid)</a>)

<a href=../02-max-open-files/>» Next Slide</a>
