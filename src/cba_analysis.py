def calculate_cba(ale_prior: float, ale_post: float, acs: float) -> float:
    """
    Calculate the Cost-Benefit Analysis (CBA) for risk mitigation.
    Formula: CBA = ALE_prior - ALE_post - ACS
    """
    return ale_prior - ale_post - acs

if __name__ == "__main__":
    ale_prior = 50000  
    ale_post = 10000   
    acs = 15000       
    cba_result = calculate_cba(ale_prior, ale_post, acs)
    print(f"Cost-Benefit Analysis Result: ${cba_result:,.2f}")
