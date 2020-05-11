// Description:
// Were you ever interested in the phenomena of astrology, star signs, tarot, voodoo ? (ok not voodoo that's too spooky)...
// Task:
// Your job for today is to finish the starSign function by finding the astrological sign, given the birth details as a Date object.
// Start and end dates for zodiac signs vary on different resources so we will use this table to get consistent results:

// Aquarius ------ 21 January - 19 February
// Pisces --------- 20 February - 20 March
// Aries ---------- 21 March - 20 April
// Taurus -------- 21 April - 21 May
// Gemini -------- 22 May - 21 June
// Cancer -------- 22 June - 22 July
// Leo ------------- 23 July - 23 August
// Virgo ----------- 24 August - 23 September
// Libra ----------- 24 September - 23 October
// Scorpio -------- 24 October - 22 November
// Sagittarius ---- 23 November - 21 December
// Capricorn ----- 22 December - 20 January

// Test info: 100 random tests (dates range from January 1st 1940 until now)

// SOLUTION
function starSign(date) {
  const starSigns = ['Aquarius-21','Pisces-20','Aries-21','Taurus-21','Gemini-22','Cancer-22','Leo-23','Virgo-24','Libra-24','Scorpio-24','Sagittarius-23','Capricorn-22']
  const starDate = Number(starSigns[date.getMonth()].split('-')[1])
  if (date.getDate() < starDate && date.getMonth() === 0) return 'Capricorn'
  return date.getDate() < starDate ? starSigns[date.getMonth() - 1].split('-')[0] : starSigns[date.getMonth()].split('-')[0]
}