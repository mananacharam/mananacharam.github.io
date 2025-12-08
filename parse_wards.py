import re
import json
import os

def parse_ward_file(filepath):
    """Parse a ward file and extract voter data"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Extract header information
    content = ''.join(lines)
    mandal_match = re.search(r'Mandal\s*:\s*([^\n]+)', content)
    gram_panchayat_match = re.search(r'Gram Panchayat\s*:\s*([^\n]+)', content)
    ward_match = re.search(r'Ward No\.\s*:\s*([^\n]+)', content)
    electors_match = re.search(r'No\. of Electors\s*:\s*(\d+)', content)
    
    # Extract summary statistics
    men_match = re.search(r'Male\s+(\d+)', content)
    women_match = re.search(r'Female\s+(\d+)', content)
    others_match = re.search(r'Others\s+(\d+)', content)
    total_match = re.search(r'Total Voters in Voter List\s+(\d+)', content)
    
    # Parse individual voter records line by line
    voters = []
    current_voter = None
    i = 0
    
    while i < len(lines):
        line = lines[i].rstrip('\n\r')
        
        # Check if this is a new voter entry (starts with number followed by A.C No.)
        # Handle tabs and spaces - note: PS No. and SLNo. have spaces around the dash
        voter_start = re.match(r'^(\d+)\s+A\.C No\.:\s*-(\d+)\s+PS No\.:\s*-\s*(\d+)\s+SLNo\.:\s*-\s*(\d+)$', line)
        
        if voter_start:
            # Save previous voter if exists and complete
            if current_voter and 'name' in current_voter and 'epic_no' in current_voter:
                voters.append(current_voter)
            
            # Start new voter
            current_voter = {
                'serial_no': int(voter_start.group(1)),
                'ac_no': int(voter_start.group(2)),
                'ps_no': int(voter_start.group(3)),
                'sl_no': int(voter_start.group(4))
            }
            i += 1
            continue
        
        # Only process if we have an active voter
        if current_voter is None:
            i += 1
            continue
        
        line_stripped = line.strip()
        
        # Parse Name
        if line_stripped == 'Name' and i + 1 < len(lines):
            name_line = lines[i + 1].strip()
            if name_line.startswith(':'):
                current_voter['name'] = name_line[1:].strip()
                i += 2
                continue
        
        # Parse relationship (Father/Husband/Mother/Wife/Others)
        if line_stripped in ['Father Name', 'Husband Name', 'Mother Name', 'Wife Name', 'Others'] and i + 1 < len(lines):
            rel_line = lines[i + 1].strip()
            if rel_line.startswith(':'):
                current_voter['relationship_type'] = line_stripped
                current_voter['relationship_name'] = rel_line[1:].strip()
                i += 2
                continue
        
        # Parse Age and Sex
        if line_stripped == 'Age' and i + 1 < len(lines):
            age_line = lines[i + 1].strip()
            age_sex_match = re.search(r':\s*(\d+)\s+Sex\s*:\s*:\s*([MF])', age_line)
            if age_sex_match:
                current_voter['age'] = int(age_sex_match.group(1))
                current_voter['sex'] = age_sex_match.group(2)
                i += 2
                continue
        
        # Parse Door No.
        if line_stripped == 'Door No.' and i + 1 < len(lines):
            door_line = lines[i + 1].strip()
            if door_line.startswith(':'):
                current_voter['door_no'] = door_line[1:].strip()
                i += 2
                continue
        
        # Parse EPIC No.
        if line_stripped == 'EPIC No.' and i + 1 < len(lines):
            epic_line = lines[i + 1].strip()
            if epic_line and not epic_line.startswith(':'):
                current_voter['epic_no'] = epic_line.strip()
                i += 2
                continue
        
        i += 1
    
    # Add last voter if complete
    if current_voter and 'name' in current_voter and 'epic_no' in current_voter:
        voters.append(current_voter)
    
    return {
        'mandal': mandal_match.group(1).strip() if mandal_match else '',
        'gram_panchayat': gram_panchayat_match.group(1).strip() if gram_panchayat_match else '',
        'ward_no': ward_match.group(1).strip() if ward_match else '',
        'total_electors': int(electors_match.group(1)) if electors_match else 0,
        'summary': {
            'male': int(men_match.group(1)) if men_match else 0,
            'female': int(women_match.group(1)) if women_match else 0,
            'others': int(others_match.group(1)) if others_match else 0,
            'total': int(total_match.group(1)) if total_match else 0
        },
        'voters': voters
    }

def main():
    """Parse all ward files and create JSON output"""
    all_wards_data = {}
    
    # Process all ward files from Ward 1 to Ward 10
    for ward_num in range(1, 11):
        filename = f'Ward {ward_num}'
        if os.path.exists(filename):
            print(f'Processing {filename}...')
            try:
                ward_data = parse_ward_file(filename)
                all_wards_data[f'ward_{ward_num}'] = ward_data
                print(f'  Found {len(ward_data["voters"])} voters')
            except Exception as e:
                print(f'  Error processing {filename}: {e}')
        else:
            print(f'  File {filename} not found')
    
    # Save to JSON file
    output_file = 'wards_data.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_wards_data, f, indent=2, ensure_ascii=False)
    
    print(f'\nJSON data saved to {output_file}')
    print(f'Total wards processed: {len(all_wards_data)}')
    
    # Print summary
    total_voters = sum(len(ward['voters']) for ward in all_wards_data.values())
    print(f'Total voters across all wards: {total_voters}')

if __name__ == '__main__':
    main()

