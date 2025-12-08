<template>
  <div class="agriculture-section">
    <h2 class="section-title mb-4">Agriculture & Farming</h2>

    <div class="content-blocks">
      <div class="content-block block-green">
        <h3 class="block-title">Main Crops</h3>
        <div class="crops-grid">
          <div class="crop-item">
            <div class="crop-icon">🌾</div>
            <div class="crop-name">Paddy (Rice)</div>
            <div class="crop-desc">Primary crop during Kharif season. High-yield varieties grown across 300+ acres.</div>
          </div>
          <div class="crop-item">
            <div class="crop-icon">🌽</div>
            <div class="crop-name">Maize (Corn)</div>
            <div class="crop-desc">Important Rabi crop. Used for both grain and fodder production.</div>
          </div>
          <div class="crop-item">
            <div class="crop-icon">🌶️</div>
            <div class="crop-name">Chili</div>
            <div class="crop-desc">Cash crop bringing good returns. Known for quality produce.</div>
          </div>
          <div class="crop-item">
            <div class="crop-icon">🥜</div>
            <div class="crop-name">Groundnut</div>
            <div class="crop-desc">Oilseed crop grown in rotation with paddy.</div>
          </div>
        </div>
      </div>

      <div class="content-block block-blue">
        <h3 class="block-title">Irrigation & Resources</h3>
        <ul class="info-list">
          <li>
            <i class="fas fa-tint me-2"></i>
            <span><strong>Borewells:</strong> Over 150 borewells provide irrigation water</span>
          </li>
          <li>
            <i class="fas fa-tractor me-2"></i>
            <span><strong>Mechanization:</strong> Modern tractors and harvesters available</span>
          </li>
          <li>
            <i class="fas fa-leaf me-2"></i>
            <span><strong>Organic Farming:</strong> Growing interest in natural farming methods</span>
          </li>
        </ul>
      </div>

      <div class="content-block block-amber">
        <h3 class="block-title">Market Access</h3>
        <p class="block-text">
          Farmers have access to nearby mandis in Khammam and surrounding towns. 
          Government procurement centers ensure minimum support prices for major crops.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AgricultureSection'
}
</script>

<style scoped>
.agriculture-section {
  padding: 1rem 0;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: var(--gray-900);
}

.content-blocks {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 2rem;
}

.content-block {
  padding: 2rem;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}

.block-green {
  background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
}

.block-blue {
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
}

.block-amber {
  background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
}

.block-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: var(--gray-900);
}

.crops-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.crop-item {
  background: white;
  padding: 1.5rem;
  border-radius: var(--radius);
  box-shadow: var(--shadow-xs);
}

.crop-icon {
  font-size: 2.5rem;
  margin-bottom: 0.75rem;
}

.crop-name {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--gray-900);
  margin-bottom: 0.5rem;
}

.crop-desc {
  font-size: 0.875rem;
  color: var(--gray-600);
  line-height: 1.6;
}

.info-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.info-list li {
  padding: 1rem;
  background: white;
  border-radius: var(--radius);
  margin-bottom: 0.75rem;
  display: flex;
  align-items: flex-start;
  box-shadow: var(--shadow-xs);
}

.info-list li:last-child {
  margin-bottom: 0;
}

.info-list i {
  color: #3b82f6;
  margin-top: 0.125rem;
}

.block-text {
  color: var(--gray-700);
  line-height: 1.7;
  font-size: 1rem;
}

@media (max-width: 768px) {
  .content-block {
    padding: 1.5rem;
  }

  .crops-grid {
    grid-template-columns: 1fr;
  }
}
</style>

