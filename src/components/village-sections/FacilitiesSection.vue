<template>
  <div class="facilities-section">
    <h2 class="section-title mb-4">Village Facilities</h2>

    <div class="facilities-grid">
      <div class="facility-card facility-blue">
        <h3 class="facility-title">🏫 Education</h3>
        <ul class="facility-list">
          <li>Government Primary School (Classes 1-5)</li>
          <li>High School (Classes 6-10)</li>
          <li>Anganwadi Centers (3 centers for early childhood care)</li>
          <li>Adult Education Center</li>
        </ul>
      </div>

      <div class="facility-card facility-red">
        <h3 class="facility-title">🏥 Healthcare</h3>
        <ul class="facility-list">
          <li>Primary Health Center (PHC) with 2 doctors</li>
          <li>Sub-center for basic medical services</li>
          <li>ASHA workers for community health</li>
          <li>Mobile medical unit visits twice a week</li>
          <li>Veterinary dispensary for livestock care</li>
        </ul>
      </div>

      <div class="facility-card facility-purple">
        <h3 class="facility-title">🏛️ Administrative</h3>
        <ul class="facility-list">
          <li>Gram Panchayat Office</li>
          <li>Village Secretariat</li>
          <li>Revenue Office</li>
          <li>Post Office</li>
        </ul>
      </div>

      <div class="facility-card facility-green">
        <h3 class="facility-title">🚰 Infrastructure</h3>
        <ul class="facility-list">
          <li>Piped water supply to all households</li>
          <li>Electricity with 24/7 connection</li>
          <li>Paved village roads</li>
          <li>Street lighting throughout village</li>
          <li>Community Hall for gatherings</li>
          <li>Public Library</li>
        </ul>
      </div>

      <div class="facility-card facility-yellow">
        <h3 class="facility-title">🏦 Banking & Finance</h3>
        <ul class="facility-list">
          <li>Bank branch with ATM facility</li>
          <li>Self Help Groups (SHGs) for women</li>
          <li>Cooperative society</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FacilitiesSection'
}
</script>

<style scoped>
.facilities-section {
  padding: 1rem 0;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: var(--gray-900);
}

.facilities-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.facility-card {
  padding: 2rem;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s, box-shadow 0.2s;
}

.facility-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.facility-blue {
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  border-top: 4px solid #3b82f6;
}

.facility-red {
  background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
  border-top: 4px solid #ef4444;
}

.facility-purple {
  background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);
  border-top: 4px solid #a855f7;
}

.facility-green {
  background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
  border-top: 4px solid #10b981;
}

.facility-yellow {
  background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
  border-top: 4px solid #eab308;
}

.facility-title {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--gray-900);
}

.facility-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.facility-list li {
  padding: 0.5rem 0;
  color: var(--gray-700);
  line-height: 1.7;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.facility-list li:last-child {
  border-bottom: none;
}

@media (max-width: 768px) {
  .facilities-grid {
    grid-template-columns: 1fr;
  }

  .facility-card {
    padding: 1.5rem;
  }
}
</style>

