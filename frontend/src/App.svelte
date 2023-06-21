<script>
  import TopNav from "./lib/layout/TopNav.svelte";
  import SideNav from "./lib/layout/SideNav.svelte";
  import Base from "./lib/layout/Base.svelte";
</script>

<main>
  <TopNav />
  <SideNav />
  <!-- <SideNav /> -->
  <Base />
</main>

<style>
  main {
    min-height: 100vh;
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: 6rem auto;
  }
</style>
