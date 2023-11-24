<script>
    import TopNav from "./lib/layout/TopNav.svelte";
    import SideNav from "./lib/layout/SideNav.svelte";
    import Base from "./lib/layout/Base.svelte";
    import TailwindCss from "./TailwindCSS.svelte";
</script>

<TailwindCss />

<main class="min-h-screen grid grid-rows-[6rem_auto] grid-cols-[20rem_auto]">
    <TopNav />
    <SideNav />
    <Base />
</main>
