<template>
  <header class="app-header">
    <div class="container-fluid">
      <div class="header-content">
        <h1 class="header-title">Mana Nacharam</h1>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'AppHeader'
}
</script>

<style scoped>
.app-header {
  background: linear-gradient(135deg, #1e40af 0%, #2563eb 100%);
  color: white;
  padding: 1.5rem 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.header-content {
  text-align: center;
}

.header-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0;
  letter-spacing: -0.02em;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

@media (max-width: 768px) {
  .app-header {
    padding: 1.5rem 0;
  }
  
  .header-title {
    font-size: 2rem;
  }
}
</style>

