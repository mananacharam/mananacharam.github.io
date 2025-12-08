<template>
  <div class="temples-section">
    <h2 class="section-title mb-4">Sacred Temples</h2>
    
    <div class="temples-list">
      <div class="temple-card temple-purple">
        <h3 class="temple-name">Sri Rama Temple</h3>
        <p class="temple-description">
          The main temple of our village, over 200 years old, dedicated to Lord Rama. 
          Annual Rama Navami celebrations attract devotees from surrounding villages.
        </p>
        <div class="temple-info">
          <i class="fas fa-map-marker-alt me-2"></i>
          <span>Village Center | Daily Puja: 6 AM & 7 PM</span>
        </div>
      </div>

      <div class="temple-card temple-orange">
        <h3 class="temple-name">Hanuman Temple</h3>
        <p class="temple-description">
          Located at the village entrance, this temple is visited by travelers for safe journeys. 
          Tuesday and Saturday see special prayers.
        </p>
        <div class="temple-info">
          <i class="fas fa-map-marker-alt me-2"></i>
          <span>East Entrance | Special Day: Tuesday</span>
        </div>
      </div>

      <div class="temple-card temple-blue">
        <h3 class="temple-name">Lakshmi Narasimha Swamy Temple</h3>
        <p class="temple-description">
          Ancient temple known for its architectural beauty and peaceful atmosphere. 
          Major festival during Narasimha Jayanti.
        </p>
        <div class="temple-info">
          <i class="fas fa-map-marker-alt me-2"></i>
          <span>North Side | Festival: Narasimha Jayanti</span>
        </div>
      </div>

      <div class="temple-card temple-green">
        <h3 class="temple-name">Village Goddess Temple</h3>
        <p class="temple-description">
          Dedicated to the village deity, this temple protects and blesses our community. 
          Grand celebrations during Bonalu festival.
        </p>
        <div class="temple-info">
          <i class="fas fa-map-marker-alt me-2"></i>
          <span>West Side | Festival: Bonalu</span>
        </div>
      </div>

      <div class="temple-card temple-red">
        <h3 class="temple-name">Shiva Temple</h3>
        <p class="temple-description">
          Serene temple with ancient Shivalingam. Devotees gather for Maha Shivaratri 
          and Monday prayers throughout the year.
        </p>
        <div class="temple-info">
          <i class="fas fa-map-marker-alt me-2"></i>
          <span>South Side | Special Day: Monday</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TemplesSection'
}
</script>

<style scoped>
.temples-section {
  padding: 1rem 0;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: var(--gray-900);
}

.temples-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 2rem;
}

.temple-card {
  padding: 2rem;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s, box-shadow 0.2s;
}

.temple-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.temple-purple {
  background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);
  border-left: 4px solid #a855f7;
}

.temple-orange {
  background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
  border-left: 4px solid #f97316;
}

.temple-blue {
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  border-left: 4px solid #3b82f6;
}

.temple-green {
  background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
  border-left: 4px solid #10b981;
}

.temple-red {
  background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
  border-left: 4px solid #ef4444;
}

.temple-name {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--gray-900);
}

.temple-purple .temple-name {
  color: #7c3aed;
}

.temple-orange .temple-name {
  color: #ea580c;
}

.temple-blue .temple-name {
  color: #2563eb;
}

.temple-green .temple-name {
  color: #059669;
}

.temple-red .temple-name {
  color: #dc2626;
}

.temple-description {
  color: var(--gray-700);
  line-height: 1.7;
  margin-bottom: 1rem;
}

.temple-info {
  font-size: 0.875rem;
  color: var(--gray-600);
  font-weight: 500;
}

.temple-purple .temple-info {
  color: #7c3aed;
}

.temple-orange .temple-info {
  color: #ea580c;
}

.temple-blue .temple-info {
  color: #2563eb;
}

.temple-green .temple-info {
  color: #059669;
}

.temple-red .temple-info {
  color: #dc2626;
}

@media (max-width: 768px) {
  .temple-card {
    padding: 1.5rem;
  }

  .temple-name {
    font-size: 1.25rem;
  }
}
</style>

