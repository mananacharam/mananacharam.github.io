<template>
  <footer class="app-footer">
    <div class="container-fluid">
      <div class="footer-content">
        <div class="footer-section">
          <h5 class="footer-title">Voter Information System</h5>
          <p class="footer-text">Mana Nacharam Village</p>
        </div>
        <div class="footer-section">
          <h5 class="footer-title">Information</h5>
          <div class="footer-text">
            <i class="fas fa-map-marker-alt me-2"></i>
            <div class="address-text">
              Nacharam,<br>
              Dammapeta Mandal,<br>
              Bhadradri-Kothagudem,<br>
              Telangana 507306
            </div>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="footer-copyright">
          <p>&copy; 2025 Mana Nacharam Village</p>
        </div>
        <div class="footer-tagline">
          <p>Together We Grow | మనం కలిసి ఎదుగుదాం</p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'AppFooter'
}
</script>

<style scoped>
.app-footer {
  background: #1e293b;
  color: #cbd5e1;
  padding: 3rem 0 1.5rem;
  margin-top: 4rem;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.footer-section {
  display: flex;
  flex-direction: column;
}

.footer-title {
  color: white;
  font-size: 1rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.footer-text {
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
  color: #94a3b8;
  line-height: 1.6;
  display: flex;
  align-items: flex-start;
}

.address-text {
  display: inline-block;
  line-height: 1.8;
}

.footer-links {
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-links li {
  margin-bottom: 0.5rem;
}

.footer-links a {
  color: #94a3b8;
  text-decoration: none;
  font-size: 0.875rem;
  transition: color 0.2s;
}

.footer-links a:hover {
  color: white;
}

.footer-bottom {
  border-top: 1px solid #334155;
  padding-top: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.footer-copyright {
  font-size: 0.8125rem;
  color: #64748b;
}

.footer-copyright p {
  margin: 0;
}

.footer-tagline {
  font-size: 0.875rem;
  color: #94a3b8;
  font-weight: 500;
}

.footer-tagline p {
  margin: 0;
}

@media (max-width: 768px) {
  .app-footer {
    padding: 2rem 0 1rem;
  }
  
  .footer-content {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .footer-bottom {
    flex-direction: column;
    text-align: center;
  }
}
</style>

